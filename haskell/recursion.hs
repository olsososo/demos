maximum' :: (Ord a) => [a] -> a
maximum' [] = error "mumimum of empty list"
maximum' [x] = x
maximum' (x:xs)
	| x > maxTail = x
	| otherwise = maxTail
	where maxTail = maximum' xs
