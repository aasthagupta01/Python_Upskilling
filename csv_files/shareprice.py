"""returns the maximum of the given arguments"""
def calc_max(*args):
    return max(*args)

def find_highest_price(csv:str):
    with open(csv, "r") as file:
        lines = file.readlines()
        for line in lines:
            newline = line.strip().split(',')
            year, month = newline[0], newline[1]
            d = {newline[2]: "company A", newline[3]: "company B", newline[4]: "company C"}
            max = calc_max(newline[2], newline[3], newline[4])
            print(d[max], month, year)

if __name__ == "__main__":
    find_highest_price("shareprice.csv")

