#5) Banking System Transactions:
# A banking system stores a customer's transactions in a single string. 
# Each transaction is represented as: <type><amount> where: D indicates Deposit, W indicates Withdrawal and The amount is an integer. 
# Transactions are separated by commas. For example: [D500, W200, D1000, W300]. 
# The bank wants to determine the final account balance, but there is an 
# additional rule: A withdrawal should be processed only if sufficient balance is available at that point in the transaction sequence. 
# Otherwise, the transaction is rejected.  Write a function:
# def calculate_balance(transactions):that processes the transactions in the given order and 
# returns: The final balance and The number of rejected withdrawals.
# Example 1  Input: [D500, W200, D1000, W300]  Output:Balance = 1000  Rejected = 0  
# Example 2  Input: [W500, D300, W100, D1000, W800]  Output:Balance = 400  Rejected = 2 

def calculate_balance(transactions):
    balance = 0
    rejected = 0
 
    for t in transactions:
        kind = t[0]              # 'D' or 'W'
        amount = int(t[1:])      # the numeric part
 
        if kind == "D":
            balance += amount
        elif kind == "W":
            if balance >= amount:
                balance -= amount
            else:
                rejected += 1
        else:
            raise ValueError(f"Unknown transaction type in: {t!r}")
 
    return balance, rejected
 
 
def section(title):
    print("\n" + "-" * 67)
    print(title)
    print("-" * 67)
 
 
def run_case(transactions, label, expected=None, trace=False):
    print(f"{label}")
    print(f"  Input: {transactions}")
    if trace:
        # step-by-step trace, useful for verifying against a stated example
        balance, rejected = 0, 0
        for t in transactions:
            kind, amount = t[0], int(t[1:])
            if kind == "D":
                balance += amount
                print(f"    {t:>7} (deposit)     -> balance = {balance}")
            else:
                if balance >= amount:
                    balance -= amount
                    print(f"    {t:>7} (withdraw OK) -> balance = {balance}")
                else:
                    rejected += 1
                    print(f"    {t:>7} (withdraw REJECTED, balance {balance} < {amount})")
        result = (balance, rejected)
    else:
        result = calculate_balance(transactions)
 
    print(f"  Output: Balance = {result[0]}, Rejected = {result[1]}")
    if expected is not None:
        match = "OK matches expected" if result == expected else "DOES NOT match stated expected value"
        print(f"  Check:  expected {expected} -> {match}")
 
 
if __name__ == "__main__":
    section("Problem 5 — Banking System Transactions")
 
    # Example 1 from the problem statement
    run_case(
        ["D500", "W200", "D1000", "W300"],
        "Example 1 from problem statement",
        expected=(1000, 0),
    )
 
    # Example 2 from the problem statement — traced step by step
    print()
    run_case(
        ["W500", "D300", "W100", "D1000", "W800"],
        "Example 2 from problem statement (step-by-step trace)",
        expected=(400, 2),
        trace=True,
    )
    print(
        "\n  NOTE: Applying the rule exactly as described (reject a withdrawal\n"
        "  only if the running balance at that point is less than the amount)\n"
        "  gives Rejected = 1 for this input, not 2 as the prompt states —\n"
        "  only 'W500' fails (balance is 0); 'W100' succeeds once balance is\n"
        "  300, and 'W800' succeeds once balance is 1200. Balance = 400 does\n"
        "  match. Worth double-checking the intended numbers for Example 2."
    )
 
    # Additional edge cases
    print()
    run_case([], "No transactions at all", expected=(0, 0))
    run_case(["W100"], "Single withdrawal with zero balance", expected=(0, 1))
    run_case(["D100", "W100"], "Withdraw exactly the full balance (boundary case)", expected=(0, 0))
    run_case(["D0", "W0"], "Zero-amount transactions", expected=(0, 0))
 

 
