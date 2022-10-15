# asurion-assessment

## Dataset First Impressions
- There is missing data
- There are 3 sites (east, north, south)
- There are 2 clients (A, B)
- There are 16 supervisors
  - Some seem to be mispelled
    - ANDREEW instead of Andrew
    - SARA instead of Sarah
    - JORRGE instead of Jorge
      - This could also be George
    - JONATHAN instead of John
- This data is taken over 5 weeks of time
- Service time appears to be in seconds
  - Ranges from 402 to 550
  - 9 blanks out of 240 data points
- Quality of service is scale 0-10
  - Ranges from 4.3 - 9.3
  - There are 6 blanks out of 240


## Assignment First Impressions
### Requirements
1. Generate a presentation that can appeal to technical and non-technical people that describes my findings from the dataset
2. Create a list of probing questions/opportunities for the business units to follow to try and improve service
3. Provide code used to perform the analysis

## Assumptions
1. These are the only supervisors and agents for this region
2. We are not missing data
3. These supervisors and agents work with similar customer demographics so the data is not skewed by servicing in Dallas vs Chicago



# Findings
- The core of my findings so far, the customer B has the worst service, so the largest opportunity for improvement. 
  - Usually if a customer is dissatisfied, it is more than just a service time.
  - We should meet with the customer to discuss the issues
    - If its as simple as service time, we need to get our faster/more experienced people working more consistently with them to make them happy
    - This can come at reduced happiness of the already happy customer, but it depends on priorities
- The South site has a bigger opportunity for improvement on times.
  - This could be handled one of two ways
    - See if two people from the North location would switch to balance the locations.
      - They would be tasked with training/improving the South location people
      - Those that moved from the South into the North site would be trained by the North people
      - It is hard to move people sometimes so this may not be an option
    - Focus efforts/training on the South site to get them faster and more efficient


# Next Steps
- Now that I understand the data at a cursory glance, and I have next steps labeled out, some other interesting things to do:
  - Build a predictive model that could say, based on the variables given, what quality score should you expect
  - Then it could tell you that based on the variables the Agent controls, what they can do to get a higher score


- For those statistical nerds like me out there,
- I would want to use feature reduction to try and simplify the model and remove redundancies with the correlated data
- There is only one variable in their control at this point in time so that is time.
  - It would show the expected score based on the windows seen in the plotted graph
  - I also know better than to make the expected score an exact value. It would be an "expected" range
