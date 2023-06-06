from calculation.calculate import calculate, make_plus_minus_only
from calculation.tokenize import tokenize, tokenize_with_brackets


def get_outermost_brackets(token_list):
    tmp_brackets_list = []
    outermost_left_bracket_list = []
    outermost_right_bracket_list = []
    for i in range(len(token_list)):
        if token_list[i]["type"] == "LEFT_BRACKET":
            if len(tmp_brackets_list) == 0:
                outermost_left_bracket_list.append(i)
            tmp_brackets_list.append(i)
            continue
        if token_list[i]["type"] == "RIGHT_BRACKET":
            if len(tmp_brackets_list) == 1:
                outermost_right_bracket_list.append(i)
            tmp_brackets_list.pop(-1)
            continue
    return outermost_left_bracket_list, outermost_right_bracket_list


def solve_outermost_brackets(token_list):
    outermost_left_bracket_list, outermost_right_bracket_list = get_outermost_brackets(
        token_list
    )
    assert len(outermost_left_bracket_list) == len(outermost_right_bracket_list)

    if len(outermost_left_bracket_list) == 0:  # 全ての括弧が解消してる時
        # token_list=tokenize(token_list)
        flat_list = make_plus_minus_only(token_list)
        value = calculate(flat_list)
        return [{"type": "NUMBER", "value": value}]

    else:
        if outermost_left_bracket_list[0] > 0:  # はじめが括弧から始まらない時
            new_token_list = token_list[: (outermost_left_bracket_list[0])]
        else:  # はじめが括弧から始まる時
            new_token_list = []

        for i in range(len(outermost_left_bracket_list)):
            token_list_in_brackets = token_list[
                (outermost_left_bracket_list[i] + 1) : outermost_right_bracket_list[i]
            ]
            solved_token_list = solve_outermost_brackets(token_list_in_brackets)
            new_token_list += solved_token_list
            if (i + 1) < len(outermost_left_bracket_list):  # まだ最後の外側括弧ペアに至ってない時
                new_token_list += token_list[
                    (outermost_right_bracket_list[i] + 1) : (
                        outermost_left_bracket_list[i + 1]
                    )
                ]

        if outermost_right_bracket_list[-1] == (len(token_list) - 1):  # 一番最後が括弧で終わる時
            pass
        else:  # 一番最後が括弧ではない時
            new_token_list += token_list[(outermost_right_bracket_list[-1] + 1) :]

        # return new_token_list

        flat_list = make_plus_minus_only(new_token_list)
        value = calculate(flat_list)

        return [{"type": "NUMBER", "value": value}]
