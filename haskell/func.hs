lucky :: (Integral a) => a -> String
lucky 7 = "Lucky number seven"
lucky x = "Sorry,you are out of lucky,pal!"

factorial :: (Integral a) => a -> a
factorial 0 = 1
factorial n = n * factorial (n - 1)

charName :: Char -> String
charName 'a' = "Albert"
charName 'b' = "Broseph"
charName 'c' = "Cecil"
charName c = "=.="

addVectors :: (Num a ) => (a,a) -> (a,a) -> (a,a)
addVectors (x1 ,y1) (x2, y2) = (x1 + x2,y1 + y2)

first :: (a, b, c) -> a
first (x, _, _) = x

second :: (a, b, c) -> b
second (_, y, _) = y

third :: (a, b, c) -> c
third (_, _, z) = z

head' :: [a] -> a
head' [] = error"Can not call head on an empty list,dummy!"
head' (x:_) = x
