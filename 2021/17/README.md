```
t = 0
    v_x(0), v_y(0)
    x(0), y(0) = 0, 0
t = 1
    v_x(1) = v_x(0) - 1
    v_y(1) = v_y(0) - 1
    x(1) = x(0) + v_x(0)
    y(1) = y(0) + v_y(0)
...
t
    v_x(t) = v_x(t-1) - 1
           = { v_x(0) - t if t <= v_x(0)
             { 0          if t > v_x(0)
    v_y(t) = v_y(0) - t
    x(t) = x(t-1) + v_x(t-1)
         = x(0) + v_x(0) + v_x(1) + ... + v_x(t-1)
         = { v_x(0) + (v_x(0) - 1) + ... + (v_x(0) - (t-1)) if t <= v_x(0)
           { v_x(0) + (v_x(0) - 1) + ... + 1                if t > v_x(0)
         = { (v_x(0) + v_x(0) - (t-1)) * t / 2 if t <= v_x(0)
           { (v_x(0) + 1) * v_x(0) / 2         if t > v_x(0)
         = { v_x(0) * t - t * (t-1) / 2 if t <= v_x(0)
           { v_x(0) * (v_x(0) + 1) / 2  if t > v_x(0)
    y(t) = v_y(0) * t - t * (t-1) / 2
```
Let's define the target area as
```
[X_0, X_1]
[Y_0, Y_1]
```
The target area is below the `y = 0` line, so after we fire the probe up, it will cross that line when:
```
y(t) = 0 <=> v_y(0) * t - t * (t-1) / 2 = 0
         <=> v_y(0) = (t-1) / 2
         <=> t = 2 * v_y(0) + 1
```
At that `t`:
```
v_y(2 * v_y(0) + 1) = v_y(0) - (2 * v_y(0) + 1) = -v_y(0) - 1
```

## Part 1
`v_y(0)` needs to be as high as possible and still allows the probe to reach the target area.
The highest `v_y(0)` can be is one that makes the probe reach the bottom line of the target area exactly one step
after it's at the `y = 0` line, which means:
```
v_y(2 * v_y(0) + 1) = -v_y(0) - 1 = Y_0
                   <=> v_y(0) = -Y_0 - 1
```
The highest y is reached at half the time `t = 2 * v_y(0) + 1`, but as we only consider an integer number of steps,
`t` should either be `v_y(0)` or `v_y(0) + 1`, `y` at those steps are:
```
y(v_y(0)) = v_y(0) * v_y(0) - v_y(0) * (v_y(0) - 1) / 2
          = v_y(0) * (v_y(0) + 1) / 2
y(v_y(0) + 1) = v_y(0) * (v_y(0) + 1) - (v_y(0) + 1) * (v_y(0) + 1 - 1) / 2
              = v_y(0) * (v_y(0) + 1) / 2
```
So they are equal, and the highest y is:
```
y(v_y(0)) = y(v_y(0) + 1) = v_y(0) * (v_y(0) + 1) / 2
                          = (-Y_0 - 1) * (-Y_0) / 2
                          = (Y_0 + 1) * Y_0 / 2
```

## Part 2
We have two cases:
- When `t <= v_x(0)`: as we have above
```
x(t) = v_x(0) * t - t * (t-1) / 2
y(t) = v_y(0) * t - t * (t-1) / 2
=> ds = x(t) - y(t) = t * (v_x(0) - v_y(0)) = t * dv(0)
```
With `X_0 <= x(t) <= X_1` and `Y_0 <= y(t) <= Y_1`:
```
X_0 - Y_1 <= ds <= X_1 - Y_0
```
So we can loop through each value in this closed interval `[X_0 - Y_1, X_1 - Y_0]`,
find `t` and `dv(0)` values which are integers, and for each `t` we find pairs of `(v_x(0), v_y(0))`
that make `x(t)` and `y(t)` be in their respective interval.

- When `t > v_x(0)`:
```
x(t) = v_x(0) * (v_x(0) + 1) / 2
```
Find integer v_x(0) values that make `x(t)` be in `[X_0, X_1]`.
For each `t` larger than that `v_x(0)`, find `v_y(0)` values that make `y(t)` be in `[Y_0, Y_1]`.
End looping with `t` when the interval to consider for `v_y(0)` is too small.