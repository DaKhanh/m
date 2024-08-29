standard_prompt = '''
Solve the math problem: {input}
'''

cot_prompt = '''
Solve the math problem: A particle is projected vertically upwards from horizontal ground. The speed of the particle 2 seconds after it is projected is 5 m/s and it is travelling downwards. Find the speed of projection of the particle. 

Your output should be of the following format:

Steps:
1. Understand the Given Information:
The particle is projected upwards.
After 2 seconds, the particle's speed is 5 m/s, and it is traveling downwards.
The acceleration due to gravity g is 9.8 m/s^2 (assuming Earth's gravity).

2. Apply the Equations of Motion:
We know that the velocity of a particle under constant acceleration is given by: v=u-gt

3. Substitute the Given Values:
At t=2 seconds, the particles velocity v is -5 m/s (since it is traveling downwards): -5=u-9.8*2

4. Solve for the Initial Speed u: -5=u-19.6; u=-19.6+5=14.6 m/s

Conclusion: The speed of projection of the particle is 14.6 m/s.

Solve the math problem: {input}

Your output should be of the following format:

Steps:
Your steps here.

Conclusion:
Your conclusion here.
'''

tot_initial_prompt = '''
Problem: What is the value of xx in the equation 2x+3=112x+3=11?
Initial Thoughts:

    First Thought: I could solve for xx by isolating it on one side of the equation.
    Second Thought: I might also try substituting values to check which one satisfies the equation.
    Third Thought: I could graph the equation and visually inspect the solution.
    
Problem: {input}
Initial Thoughts:
'''

tot_evaluate_prompt = '''
Evaluating Each Thought:

    Isolating xx:
        Subtract 3 from both sides: 2x=82x=8.
        Divide both sides by 2: x=4x=4.
        This approach is direct and simple. Promising Path.

    Substituting Values:
        Try x=4x=4: 2(4)+3=8+3=112(4)+3=8+3=11. Correct.
        Try x=5x=5: 2(5)+3=10+3=132(5)+3=10+3=13. Incorrect.
        This method works but is less efficient. Less Promising Path.

    Graphical Approach:
        Graph y=2x+3y=2x+3 and find where y=11y=11.
        Visual method, but not as efficient for this simple equation. Less Promising Path.

Conclusion:
Based on evaluating all thoughts, the best approach is to solve for xx directly by isolating it on one side of the equation. The solution is x=4x=4

Evaluating Each Thought:
Conclusion:
'''