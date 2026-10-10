"""获取最近一个月的 BTC 日线行情，保存为 CSV 并绘制 K 线图。"""
from datetime import datetime, timedelta, timezone  # 时间计算
from pathlib import Path  # 路径处理

import mplfinance as mpf  # K 线图绘制
import pandas as pd  # 数据处理
import requests  # HTTP 请求

OUT_DIR = Path(__file__).parent  # 输出目录：脚本所在目录
SYMBOL = "BTCUSDT"  # Binance 交易对
DAYS = 30  # 获取最近多少天的数据


def fetch_binance(days: int) -> pd.DataFrame:
    end = datetime.now(timezone.utc)  # 结束时间：当前 UTC 时间
    start = end - timedelta(days=days)  # 起始时间：往前推 days 天
    resp = requests.get(
        "https://api.binance.com/api/v3/klines",  # Binance K 线接口
        params={
            "symbol": SYMBOL,  # 交易对
            "interval": "1d",  # 日线
            "startTime": int(start.timestamp() * 1000),  # 起始时间（毫秒时间戳）
            "endTime": int(end.timestamp() * 1000),  # 结束时间（毫秒时间戳）
            "limit": 1000,  # 单次最多返回条数
        },
        timeout=15,  # 超时时间（秒）
    )
    resp.raise_for_status()  # HTTP 状态码异常时抛出错误
    df = pd.DataFrame(
        resp.json(),  # 返回的是二维数组，每行一根 K 线
        columns=["ts", "Open", "High", "Low", "Close", "Volume", "close_ts",
                 "quote_vol", "trades", "taker_base", "taker_quote", "ignore"],  # Binance 返回的字段顺序
    )
    df.index = pd.to_datetime(df["ts"], unit="ms")  # 开盘时间作为时间索引
    return df[["Open", "High", "Low", "Close", "Volume"]].astype(float)  # 只保留 OHLCV 并转为数值


def fetch_okx(days: int) -> pd.DataFrame:
    resp = requests.get(
        "https://www.okx.com/api/v5/market/candles",  # OKX K 线接口
        params={"instId": "BTC-USDT", "bar": "1Dutc", "limit": days + 1},  # UTC 日线，多取一根保证覆盖
        timeout=15,  # 超时时间（秒）
    )
    resp.raise_for_status()  # HTTP 状态码异常时抛出错误
    rows = resp.json()["data"]  # 取出 K 线数据列表
    df = pd.DataFrame(rows).iloc[:, :6]  # 只取前 6 列：时间、开、高、低、收、成交量
    df.columns = ["ts", "Open", "High", "Low", "Close", "Volume"]  # 重命名列
    df.index = pd.to_datetime(df["ts"].astype("int64"), unit="ms")  # 毫秒时间戳转时间索引
    return df.drop(columns="ts").astype(float).sort_index()  # OKX 返回倒序，需按时间升序排列


def fetch_data(days: int = DAYS) -> pd.DataFrame:
    # Binance 在部分地区不可访问，失败时回退到 OKX
    for fetcher in (fetch_binance, fetch_okx):  # 按优先级依次尝试数据源
        try:
            df = fetcher(days)  # 获取数据
            print(f"数据来源: {fetcher.__name__[6:]}，共 {len(df)} 根日K线")  # 去掉 "fetch_" 前缀显示来源
            return df  # 成功即返回
        except Exception as e:
            print(f"{fetcher.__name__} 获取失败: {e}")  # 失败则打印原因并尝试下一个
    raise RuntimeError("所有数据源均获取失败")  # 全部失败


def main() -> None:
    df = fetch_data()  # 获取近一个月数据
    df.index.name = "Date"  # 索引命名，CSV 表头更清晰
    csv_path = OUT_DIR / "btc_1month.csv"  # CSV 输出路径
    png_path = OUT_DIR / "btc_kline.png"  # 图片输出路径
    df.to_csv(csv_path)  # 保存数据到本地

    # 红涨绿跌（国内习惯）
    style = mpf.make_mpf_style(
        base_mpf_style="yahoo",  # 基于 yahoo 风格
        marketcolors=mpf.make_marketcolors(up="red", down="green", inherit=True),  # 上涨红、下跌绿
    )
    mpf.plot(
        df,
        type="candle",  # 蜡烛图（K 线）
        mav=(5, 10),  # 5 日、10 日均线
        volume=True,  # 下方显示成交量
        style=style,  # 应用上面的配色
        title=f"BTC/USDT Daily K-Line (last {DAYS} days)",  # 图标题
        ylabel="Price (USDT)",  # 价格轴标签
        ylabel_lower="Volume",  # 成交量轴标签
        savefig=dict(fname=str(png_path), dpi=150),  # 保存为图片
    )
    print(f"CSV 已保存: {csv_path}\n图片已保存: {png_path}")

    mpf.plot(df, type="candle", mav=(5, 10), volume=True, style=style,
             title=f"BTC/USDT Daily K-Line (last {DAYS} days)")  # 再绘制一次，弹出窗口交互查看


if __name__ == "__main__":
    main()  # 脚本入口
