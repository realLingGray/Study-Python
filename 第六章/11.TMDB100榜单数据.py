"""读取 TMDB TOP100 电影数据，绘制年份、语言、类型和评分统计图。

将 movie_list.csv 放在本脚本同级的 data 文件夹中，然后运行本脚本。
也可以在 Jupyter 中调用 main(csv_path)，指定 CSV 文件路径。
"""

from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.axes import Axes
from matplotlib.ticker import MaxNLocator


DEFAULT_CSV_PATH = Path(__file__).resolve().parent / "data" / "movie_list.csv"


def load_data(csv_path=DEFAULT_CSV_PATH):
    """读取所需字段；上映年份使用支持空值的 Int64 类型。"""
    data = pd.read_csv(
        csv_path,
        usecols=["电影名", "上映年份", "类型", "评分", "语言"],
        dtype={"上映年份": "Int64"},
    )
    if data.empty:
        raise ValueError("CSV 文件中没有电影数据。")
    return data


def show_no_data(ax: Axes, title):
    """在没有有效数据时显示提示。"""
    ax.set_title(title, fontsize=18)
    ax.text(0.5, 0.5, "暂无有效数据", ha="center", va="center", transform=ax.transAxes)
    ax.set_axis_off()


def plot_year_count(data, ax: Axes):
    """统计每年上映的电影数量，用折线图展示，中间缺失年份补零。"""
    year_count = data.groupby("上映年份").size().sort_index()
    if year_count.empty:
        show_no_data(ax, "每年上映的电影数量")
        return

    years = list(range(int(year_count.index.min()), int(year_count.index.max()) + 1))
    counts = year_count.reindex(years, fill_value=0)
    ax.plot(years, counts.values, color="green")
    ax.set_title("每年上映的电影数量", fontsize=18)
    ax.set_xlabel("年份")
    ax.set_ylabel("电影数量")
    ax.set_xticks(years[::3])
    ax.tick_params(axis="x", rotation=45)
    ax.set_ylim(bottom=0)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.grid(linestyle="--", alpha=0.5)


def plot_language_count(data, ax: Axes):
    """按数量降序展示语言分布，与原代码一致使用电影数量作纵轴。"""
    language_count = data.groupby("语言").size().sort_values(ascending=False)
    if language_count.empty:
        show_no_data(ax, "语言分布情况")
        return

    ax.bar(language_count.index.astype(str), language_count.values, width=0.6)
    ax.set_title("语言分布情况", fontsize=18)
    ax.set_xlabel("语言", fontsize=14)
    ax.set_ylabel("电影数量", fontsize=14)
    ax.tick_params(axis="x", rotation=45)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.grid(axis="y", linestyle="--", alpha=0.5)
    ax.set_axisbelow(True)


def plot_type_count(data, ax: Axes):
    """以“和”分隔电影类型；一部电影可计入多个类型，忽略空值。"""
    type_count = {}
    for types in data["类型"].dropna().astype(str):
        for movie_type in types.split("和"):
            movie_type = movie_type.strip()
            if movie_type:
                type_count[movie_type] = type_count.get(movie_type, 0) + 1

    if not type_count:
        show_no_data(ax, "不同类型的电影数量")
        return

    ax.bar(list(type_count.keys()), list(type_count.values()), width=0.6)
    ax.set_title("不同类型的电影数量", fontsize=18)
    ax.set_xlabel("类型", fontsize=14)
    ax.set_ylabel("电影数量", fontsize=14)
    ax.tick_params(axis="x", rotation=90)
    ax.yaxis.set_major_locator(MaxNLocator(integer=True))
    ax.grid(axis="y", linestyle="--", alpha=0.5)
    ax.set_axisbelow(True)


def plot_rating_share(data, ax: Axes):
    """统计各评分的电影数量并绘制占比饼图，忽略缺失评分。"""
    rating_count = data.groupby("评分").size().sort_index()
    if rating_count.empty:
        show_no_data(ax, "各个评分占比")
        return

    labels = rating_count.index.astype(str)
    wedges, _, _ = ax.pie(rating_count.values, labels=labels, autopct="%.2f%%")
    ax.set_title("各个评分占比", fontsize=18)
    ax.set_xlabel("评分", fontsize=14)
    ax.set_ylabel("占比", fontsize=14)
    ax.axis("equal")
    ax.legend(wedges, labels, title="评分", loc="center left", bbox_to_anchor=(1, 0.5))


def create_dashboard(data):
    """创建 2×2 统计图，返回 Figure 和子图数组，便于进一步修改或保存。"""
    plt.rcParams["font.sans-serif"] = ["SimHei"]
    plt.rcParams["axes.unicode_minus"] = False

    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(16, 8), dpi=100)
    fig.suptitle("TMDB-TOP100电影榜单数据统计", fontsize=16, x=0.5, y=0.98)
    plot_year_count(data, axes[0, 0])
    plot_language_count(data, axes[0, 1])
    plot_type_count(data, axes[1, 0])
    plot_rating_share(data, axes[1, 1])
    fig.tight_layout(rect=(0, 0, 1, 0.94), h_pad=2.0)
    return fig, axes


def main(csv_path=DEFAULT_CSV_PATH):
    """读取数据、生成统计图并显示。"""
    data = load_data(csv_path)
    fig, axes = create_dashboard(data)
    plt.savefig("tmdb_top100_dashboard.png")
    plt.show()
    return fig, axes


if __name__ == "__main__":
    main()
