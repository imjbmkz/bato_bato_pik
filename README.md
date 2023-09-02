# bato_bato_pik
Bato-Bato Pik is a Python console game which was developed for the Python crash course conducted by Josh Dev (that's me!)

Run the program from the terminal.
`python bato_bato_pick_game.py`

When prompted, add your name.
`Please enter your name: `

For each round, choose your hand: `[B]ato`, `[G]unting`, or `[P]apel`. Option is case insensitive and you can add the initials too. 
`Please choose [B]ato, [G]unting, or [P]apel:`

This will run for 10 rounds. Change the value of the `ROUNDS` variable to any `int` value you want.

The results of each round is printed on the console. You can either win, lose, or the round could be a tie.
```
Please choose [B]ato, [G]unting, or [P]apel: p
You have selected Papel
Bot has selected Papel
No one wins. It's a tie
Please choose [B]ato, [G]unting, or [P]apel: 
```

On the final round, results are tallied and the winner of the game is printed. The game is then ended.
```
Please choose [B]ato, [G]unting, or [P]apel: p
You have selected Papel
Bot has selected Gunting
You lose!
Your final score is 0.
Master Bot's final score is 4.
You lost the tournament! Master Bot defeated you!
Game has ended
```
