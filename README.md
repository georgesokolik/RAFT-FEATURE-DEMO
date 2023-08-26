# RAFT REVIEW AUTO-RESPONSE (REVU) & SUMMARY REPORT
RAFT feature demo (RevU) of auto-generated Google/Yelp review responses + auto-generated summary report.

Personal NLP & ML algorithms have been removed and replaced with 3rd party OpenAI davinci-003 model API for several reasons:
- More computationally scalable for large amounts of review inputs e.g. for an exceptionally popular business
- More efficient with parallel responses at a given time
- OpenAI have enabled the opportunity to train their models with users' own training data - the same benefit with less of a headache
- LLM model has ability to detect review sentiment + provide appropriate response - two distinct features in one package
- The required training data to reliably train a natural language model up to a product standard is of a computationally taxing size for my machine - virtual machines are not a comfortable long-term solution

