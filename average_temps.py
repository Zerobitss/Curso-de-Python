def average_temps(temps):
    sum_temps = 0
    for temp in temps:
        sum_temps += temp
    return sum_temps / len(temps)
def run():
    temps = [21, 24, 25, 22, 20, 23, 26]
    average = average_temps(temps)
    print(f"La temperatura promedio es: {average}")
if __name__ == '__main__':
    run()