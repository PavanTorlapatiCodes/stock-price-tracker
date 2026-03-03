def check_alert(price, threshold):

    if price > threshold:
        return f"ALERT: Price crossed above {threshold}"

    elif price < threshold:
        return f"Price below threshold {threshold}"

    else:
        return "No alert triggered"