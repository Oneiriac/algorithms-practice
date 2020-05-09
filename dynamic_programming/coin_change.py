from typing import List

memo: List[int] = None
coins: List[int] = None


def coin_change(coins: List[int], amount: int) -> int:
    """
    Coin change DP problem with both top down and bottom up solutions.
    Recurrence: C(x) = 1 + min(C(x-D1), C(x-D2) ... C(x-Dn))
        where x is the value you need to give change for,
        D is the set of coin denominations available to choose from,
        and n is the length of D.
    """
    memo = [-1]*(amount+1)
    memo[0] = 0  # For 0 money, give 0 coins

    def coin_change_top_down(amount: int) -> int:
        # Top down recursive DP solution
        if amount < 0:
            return -1
        memo_value = memo[amount]
        if memo_value >= 0:
            return memo_value
        prev_memo_values = [coin_change_top_down(
            amount-d) for d in coins]
        options = [v for v in prev_memo_values if v >= 0]
        if len(options) == 0:
            return -1
        else:
            solution = 1 + min(options)
        memo[amount] = solution
        return memo[amount]

    def coin_change_bottom_up(amount: int) -> int:
        """Bottom-up iterative solution"""
        for x in range(1, amount+1):
            # Exclude any negative indices
            prev_memo_values = [memo[x-d] for d in coins if x-d >= 0]
            # Exclude any values that had no solutions
            options = [v for v in prev_memo_values if v >= 0]
            if len(options) == 0:  # No options/solutions
                memo[x] = -1
            else:
                memo[x] = 1 + min(options)
        return memo[amount]

    # return coin_change_top_down(amount)
    return coin_change_bottom_up(amount)


if __name__ == "__main__":
    test_coins_1 = [1, 2, 5]
    test_amount_1 = 11
    test_result_1 = coin_change(test_coins_1, test_amount_1)
    assert test_result_1 == 3

    test_coins_2 = [2]
    test_amount_2 = 3
    test_result_2 = coin_change(test_coins_2, test_amount_2)
    assert test_result_2 == -1
