# Python Project: Advanced Retrieval Augmented Generation


This is a code along with the Udemy Couse `Advanced Retrieval Augmented Generation` to get a better understanding of the advantages that llms might have for algorithmic trading.

The purpose of this repository is to document my learning journey of the practical use of LLMs.

## How to make Advanced RAG work in practice with Evaluations, Agentic Patterns and Generative AI with LLM

Coding along with the Udemy Course [Advanced Retrieval Augmented Generation ](https://www.udemy.com/course/advanced-retrieval-augmented-generation/) by Rémi Connesson.

## Problems with LLM calls that need to get solved:

1. Response time is too slow: can be solved with __asynchronous code__ and asyncio's `gather` functionality.
2. Having to pay repeatedly for the same prompt: can be solved by using __caching__.
3. It's not possible to inspect past results can be solved by using __tracing__.
4. Code is brittle. It might fail because of simple network error or rate limit: can be solved by using __retrying__.
5. I want to have some kind of structure in the outputs (structured outputs).


## Disclaimer

Code examples and comments are borrowed from the Udemy course [Advanced Retrieval Augmented Generation ](https://www.udemy.com/course/advanced-retrieval-augmented-generation/).


