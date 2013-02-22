train <- read.csv("train.csv", header=T, sep=";")
test <- read.csv("test.csv", head=T, sep=";")

library(e1071)
sv  <- svm(res ~ ., data = train, cachesize = 4096)
predictions <- predict(sv, test)

# print(predictions)
cat(predictions, file="./rrr2_.csv", sep="\n")



