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

tell :: (Show a) => [a] -> String
tell [] = "The list is empty"
tell (x:[]) = "The list has one element: " ++ show x
tell (x:y:[]) = "The list has two elements: " ++ show x ++ " and " ++ show y
tell (x:y:_) = "This list is long..."

length' :: (Num b) => [a] -> b
length' [] = 0
length' (_:xs) = 1 + length' xs

sum' :: (Num a) => [a] -> a
sum' [] = 0
sum' (x:xs) = x + sum' xs

capital :: String -> String
capital "" = "Empty string,whoops!"
capital all@(x:xs) = "The first letter of " ++ all ++ " is " ++ [x]

bmiTell :: (RealFloat a) => a -> a -> String
bmiTell weight height
	| bmi <= skinny = "You are unserweight, you emo, you!"
	| bmi <= normal = "You are supposedly normal.pffft, I bet you are ugly!"
	| bmi <= fat = "you are fat! Lose some weight,fatty!"
	| otherwise = "You are a whale,congratulations!"
	where bmi = weight / height ^ 2   
	      skinny = 18.5
	      normal = 25.0
	      fat = 30.0
	
max' :: (Ord a) => a -> a -> a
max' a b
	| a > b     = a
	| otherwise = b 

myCompare :: (Ord a) => a -> a -> Ordering 
a `myCompare` b
	| a > b	    = GT
	| a == b     = EQ
	| otherwise = LT

initials :: String -> String -> String
initials firstname lastname = [f] ++ "." ++ [l] ++ "."
	where (f:_) = firstname
	      (l:_) = lastname

calcBmis :: (RealFloat a) => [(a, a)] -> [a]
calcBmis xs = [bmi w h | (w, h) <- xs]
	where bmi weight height = weight / height ^ 2

cylinder :: (RealFloat a ) =>  a -> a -> a
cylinder r h =
	let sideArea = 2 * pi * r * h
	    topArea = pi * r ^ 2
 	in sideArea + 2 * topArea

calcBmi :: (RealFloat a) => [(a,a)] -> [a]
calcBmi xs = [bmi | (w,h) <- xs, let bmi = w /h ^ 2]
