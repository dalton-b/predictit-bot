## PredictIt-Bot Spec

This is a program that probes the website predictit.org daily to collect data.
I'm planning to use this data to run some experiments.

### Experiment 1
__Hypothesis__: The aggregate of the website users estimates are usually correct.

__Experimental Design__: I want to look at closed markets with defined closing dates. Of these markets, I will check the contract values 30 days before the close of that market and select the contract with the highest share price as the Contract of Choice. I will take the difference the final CoC value and the current CoC value, that is, final_CoC - current_CoC. This will yield the profit (either positive or negative) earned by investing in the most popular choice. Aggregated over all available markets in the dataset, this will yield the profit earned by always following the crowd 30 days before a market closes.

I will repeat this process for 60 and 90 days to market close.
