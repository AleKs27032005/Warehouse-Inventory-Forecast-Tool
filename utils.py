import matplotlib.pyplot as plt

def plot_inventory_forecast(item_name, sales_history):
    """
    Plot historical sales trend for selected item.
    """
    days = range(1, len(sales_history) + 1)

    fig, ax = plt.subplots()
    ax.plot(days, sales_history, marker="o")
    ax.set_title(f"Sales History – {item_name}")
    ax.set_xlabel("Days")
    ax.set_ylabel("Units Sold")
    ax.grid(True)

    return fig
