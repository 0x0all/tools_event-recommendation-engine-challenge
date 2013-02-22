train <- read.csv("train.csv", header=T, sep=";")
test <- read.csv("test.csv", head=T, sep=";")

library(randomForest)  
rf <- randomForest( res ~ ., train, mtry = 3, cachesize = 4096)  
predictions <- predict(rf, test)
# importance(rf)
# print(predictions)
cat(predictions, file="./rrr_.csv", sep="\n")

