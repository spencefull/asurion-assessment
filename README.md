# asurion-assessment

- The core of my findings so far, the customer B has a greater opportunity for improvement in service. 
Usually if a customer is dissatisfied, it is more than just a service time.
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


- Now that I understand the data at a cursory glance, and I have next steps labeled out, some other interesting things to do:
  - Build a predictive model that could say, based on the variables given, what quality score should you expect
  - Then it could tell you that based on the variables the Agent controls, what they can do to get a higher score


- For those statistical nerds like me out there,
- I would want to use feature reduction to try and simplify the model and remove redundancies with the correlated data
- There is only one variable in their control at this point in time so that is time.
    # It would show the expected score based on the windows seen in the plotted graph
    # I also know better than to make the expected score an exact value. It would be an "expected" range
