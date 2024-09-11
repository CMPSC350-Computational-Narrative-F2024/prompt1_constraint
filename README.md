# Prompt 1: Computational Constraint

## DUE: September 12th by 12pm

> With a good ventriloquist ... [the] puppet seems to come alive and seems to be aware of its world.
>
> Michael Graziano, in _Do Large Language Models Understand Us?_ (Blaise Agüera y Arcas)

> Prompt engineering: because even a billion-dollar AI needs you to hold its hand and use tiny words to avoid a total meltdown.
>
> GPT-4, in response to the prompt "What is prompt engineering for large language models? Answer in a very snarky way in one sentence."

## Readings

### Theory

* [Do Large Language Models Understand Us?](https://drive.google.com/file/d/1MGgIEC8ffcHfrLq1jy_8RBVKGU2R_ha9/view?usp=share_link)
* [A Brief Guide to the OULIPO](https://poets.org/text/brief-guide-oulipo)

### Practice

* [Methods of Prompt Programming](https://www.promptingguide.ai/techniques/zeroshot)
* [A compendium of various "traditional" constraints](https://drive.google.com/file/d/1OkfNSdAsUwKFfMlIHlgBDbr8yecYWNLl/view?usp=sharing)

### Documentation

* [OpenAI Completion API](https://platform.openai.com/docs/guides/chat-completions)
* [OpenAI Notes on prompt design](https://platform.openai.com/docs/guides/prompt-engineering/six-strategies-for-getting-better-results)

## Summary

To date, successful prompt engineering endeavors to ask what an individual _wants_ to happen. This assignment approaches generative writing with large language models (LLM) from an opposite perspective. Drawing on the practice of the _Ouvroir de littérature potentielle_ ("Oulipo"), we challenge GPT to a more difficult task—producing works of "constrained" writing to discover what LLM can and, more importantly, cannot do. 

For those of us familiar with visual image generators such as DALLE or Stable Diffusion, this idea is close to, but not quite "negative prompting" (e.g. asking for a picture of a house without any people in it). The approach of computational constraint applied to language prompts thinks about the concept _generatively_. We aren't simply asking to "live without" a feature common to a parcel of language, we're interested in rethinking the possibilities are open by _restricting choice_.

Mainly, what kinds of choices can we engineer the model to make and how can we account for those choices?

## Goals

* Learn to interact with LLM through the practice of prompt engineering
* Refine skills in prompt engineering to increase efficacy and quality of output
* Discover exploitable boundaries in LLM generation
* Develop a model of a constraint as an enabling practice

## Tasks

* 2 poems and corresponding prompts (included in the `writing` folder as `md` files)
    * 1 enacting a ["traditional" Oulipean constraint](https://drive.google.com/file/d/1OkfNSdAsUwKFfMlIHlgBDbr8yecYWNLl/view?usp=sharing)
    * 1 enacting a constraint only possible using GPT

Please note that you may ask the model to generate the poem or you may put some existing text to be used for the constraint in `src/data`.

Please remember that `main.py` requires the creation of an `.env` file, as was done in project 1.
