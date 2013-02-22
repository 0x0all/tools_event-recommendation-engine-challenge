train <- read.csv("train.csv", header=T, sep=";")
test <- read.csv("test.csv", head=T, sep=";")

library(caret)
kn  <- knnregTrain(train, test, 7, k = 10, use.all=T)
predictions <- predict(kn, test)

cat(predictions, file="./rrr3_.csv", sep="\n")
