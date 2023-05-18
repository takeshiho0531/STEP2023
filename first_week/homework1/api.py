from fastapi import FastAPI

from first_week.homework1.anagram import main  # TODO: 関数名..

router = FastAPI(tags=["anagram_checker"])


@router.post("/anagram_checker/query")
def anagram_checker_query(query_word: str) -> str:
    answer = main(query_word)
    return answer
