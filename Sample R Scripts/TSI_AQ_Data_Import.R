# Author: Nelsha Athauda
# Date: 05/16/2023
# Purpose: Import TSI Air Quality Monitor SD Card Data

here::i_am("CTR-IN - indoor wood smoke/AQ Monitors/Script/TSI_AQ_Data_Import.R")

library(here)
library(readxl)

fileNames <- list.files(path = here("Data/SD_Card/81432223001"), full.names = TRUE)
dataList <- list()

for (fileName in fileNames) {
  data <- read.csv(fileName, header = TRUE, sep = ",", skip = 5)[-1,]
  dataList[[fileName]] <- data
}

TSI_81432223001 <- do.call(rbind, dataList)


fileNames <- list.files(path = here("Data/SD_Card/81432223002"), full.names = TRUE)
dataList <- list()

for (fileName in fileNames) {
  data <- read.csv(fileName, header = TRUE, sep = ",", skip = 5)[-1,]
  dataList[[fileName]] <- data
}

TSI_81432223002 <- do.call(rbind, dataList)


fileNames <- list.files(path = here("Data/SD_Card/81432223003"), full.names = TRUE)
dataList <- list()

for (fileName in fileNames) {
  data <- read.csv(fileName, header = TRUE, sep = ",", skip = 5)[-1,]
  dataList[[fileName]] <- data
}

TSI_81432223003 <- do.call(rbind, dataList)


fileNames <- list.files(path = here("Data/SD_Card/81432223004"), full.names = TRUE)
dataList <- list()

for (fileName in fileNames) {
  data <- read.csv(fileName, header = TRUE, sep = ",", skip = 5)[-1,]
  dataList[[fileName]] <- data
}

TSI_81432223004 <- do.call(rbind, dataList)


fileNames <- list.files(path = here("Data/SD_Card/81432223012"), full.names = TRUE)
dataList <- list()

for (fileName in fileNames) {
  data <- read.csv(fileName, header = TRUE, sep = ",", skip = 5)[-1,]
  dataList[[fileName]] <- data
}

TSI_81432223012 <- do.call(rbind, dataList)


fileNames <- list.files(path = here("Data/SD_Card/81432223005"), full.names = TRUE)
dataList <- list()

for (fileName in fileNames) {
  data <- read.csv(fileName, header = TRUE, sep = ",", skip = 5)[-1,]
  dataList[[fileName]] <- data
}

TSI_81432223005 <- do.call(rbind, dataList)


fileNames <- list.files(path = here("Data/SD_Card/81432223006"), full.names = TRUE)
dataList <- list()

for (fileName in fileNames) {
  data <- read.csv(fileName, header = TRUE, sep = ",", skip = 5)[-1,]
  dataList[[fileName]] <- data
}

TSI_81432223006 <- do.call(rbind, dataList)


fileNames <- list.files(path = here("Data/SD_Card/81432223008"), full.names = TRUE)
dataList <- list()

for (fileName in fileNames) {
  data <- read.csv(fileName, header = TRUE, sep = ",", skip = 5)[-1,]
  dataList[[fileName]] <- data
}

TSI_81432223008 <- do.call(rbind, dataList)


fileNames <- list.files(path = here("Data/SD_Card/81432223009"), full.names = TRUE)
dataList <- list()

for (fileName in fileNames) {
  data <- read.csv(fileName, header = TRUE, sep = ",", skip = 5)[-1,]
  dataList[[fileName]] <- data
}

TSI_81432223009 <- do.call(rbind, dataList)


fileNames <- list.files(path = here("Data/SD_Card/81432223010"), full.names = TRUE)
dataList <- list()

for (fileName in fileNames) {
  data <- read.csv(fileName, header = TRUE, sep = ",", skip = 5)[-1,]
  dataList[[fileName]] <- data
}

TSI_81432223010 <- do.call(rbind, dataList)


fileNames <- list.files(path = here("Data/SD_Card/81432223011"), full.names = TRUE)
dataList <- list()

for (fileName in fileNames) {
  data <- read.csv(fileName, header = TRUE, sep = ",", skip = 5)[-1,]
  dataList[[fileName]] <- data
}

TSI_81432223011 <- do.call(rbind, dataList)


fileNames <- list.files(path = here("Data/SD_Card/81432223018"), full.names = TRUE)
dataList <- list()

for (fileName in fileNames) {
  data <- read.csv(fileName, header = TRUE, sep = ",", skip = 5)[-1,]
  dataList[[fileName]] <- data
}

TSI_81432223018 <- do.call(rbind, dataList)


fileNames <- list.files(path = here("Data/SD_Card/81432223019"), full.names = TRUE)
dataList <- list()

for (fileName in fileNames) {
  data <- read.csv(fileName, header = TRUE, sep = ",", skip = 5)[-1,]
  dataList[[fileName]] <- data
}

TSI_81432223019 <- do.call(rbind, dataList)


fileNames <- list.files(path = here("Data/SD_Card/81432223021"), full.names = TRUE)
dataList <- list()

for (fileName in fileNames) {
  data <- read.csv(fileName, header = TRUE, sep = ",", skip = 5)[-1,]
  dataList[[fileName]] <- data
}

TSI_81432223021 <- do.call(rbind, dataList)


fileNames <- list.files(path = here("Data/SD_Card/81432223022"), full.names = TRUE)
dataList <- list()

for (fileName in fileNames) {
  data <- read.csv(fileName, header = TRUE, sep = ",", skip = 5)[-1,]
  dataList[[fileName]] <- data
}

TSI_81432223022 <- do.call(rbind, dataList)


fileNames <- list.files(path = here("Data/SD_Card/81432223027"), full.names = TRUE)
dataList <- list()

for (fileName in fileNames) {
  data <- read.csv(fileName, header = TRUE, sep = ",", skip = 5)[-1,]
  dataList[[fileName]] <- data
}

TSI_81432223027 <- do.call(rbind, dataList)


fileNames <- list.files(path = here("Data/SD_Card/81432223028"), full.names = TRUE)
dataList <- list()

for (fileName in fileNames) {
  data <- read.csv(fileName, header = TRUE, sep = ",", skip = 5)[-1,]
  dataList[[fileName]] <- data
}

TSI_81432223028 <- do.call(rbind, dataList)


fileNames <- list.files(path = here("Data/SD_Card/81432223029"), full.names = TRUE)
dataList <- list()

for (fileName in fileNames) {
  data <- read.csv(fileName, header = TRUE, sep = ",", skip = 5)[-1,]
  dataList[[fileName]] <- data
}

TSI_81432223029 <- do.call(rbind, dataList)


fileNames <- list.files(path = here("Data/SD_Card/81432223030"), full.names = TRUE)
dataList <- list()

for (fileName in fileNames) {
  data <- read.csv(fileName, header = TRUE, sep = ",", skip = 5)[-1,]
  dataList[[fileName]] <- data
}

TSI_81432223030 <- do.call(rbind, dataList)


fileNames <- list.files(path = here("Data/SD_Card/81432231001"), full.names = TRUE)
dataList <- list()

for (fileName in fileNames) {
  data <- read.csv(fileName, header = TRUE, sep = ",", skip = 5)[-1,]
  dataList[[fileName]] <- data
}

TSI_81432231001 <- do.call(rbind, dataList)


fileNames <- list.files(path = here("Data/SD_Card/81432231023"), full.names = TRUE)
dataList <- list()

for (fileName in fileNames) {
  data <- read.csv(fileName, header = TRUE, sep = ",", skip = 5)[-1,]
  dataList[[fileName]] <- data
}

TSI_81432231023 <- do.call(rbind, dataList)


fileNames <- list.files(path = here("Data/SD_Card/81432306005"), full.names = TRUE)
dataList <- list()

for (fileName in fileNames) {
  data <- read.csv(fileName, header = TRUE, sep = ",", skip = 5)[-1,]
  dataList[[fileName]] <- data
}

TSI_81432306005 <- do.call(rbind, dataList)



#Save each file as an RDS
setwd(here("CTR-IN - indoor wood smoke/AQ Monitors/Data/Aggregated_SD_Card_Data"))

saveRDS(TSI_81432223001, file = "TSI_81432223001.RDS") 
saveRDS(TSI_81432223002, file = "TSI_81432223002.RDS") 
saveRDS(TSI_81432223003, file = "TSI_81432223003.RDS") 
saveRDS(TSI_81432223004, file = "TSI_81432223004.RDS") 
saveRDS(TSI_81432223005, file = "TSI_81432223005.RDS") 
saveRDS(TSI_81432223006, file = "TSI_81432223006.RDS") 
saveRDS(TSI_81432223008, file = "TSI_81432223008.RDS") 
saveRDS(TSI_81432223009, file = "TSI_81432223009.RDS") 
saveRDS(TSI_81432223010, file = "TSI_81432223010.RDS") 
saveRDS(TSI_81432223011, file = "TSI_81432223011.RDS") 
saveRDS(TSI_81432223012, file = "TSI_81432223012.RDS") 
saveRDS(TSI_81432223018, file = "TSI_81432223018.RDS") 
saveRDS(TSI_81432223019, file = "TSI_81432223019.RDS") 
saveRDS(TSI_81432223021, file = "TSI_81432223021.RDS") 
saveRDS(TSI_81432223022, file = "TSI_81432223022.RDS") 
saveRDS(TSI_81432223027, file = "TSI_81432223027.RDS") 
saveRDS(TSI_81432223028, file = "TSI_81432223028.RDS") 
saveRDS(TSI_81432223029, file = "TSI_81432223029.RDS") 
saveRDS(TSI_81432223030, file = "TSI_81432223030.RDS") 
saveRDS(TSI_81432231001, file = "TSI_81432231001.RDS") 
saveRDS(TSI_81432231023, file = "TSI_81432231023.RDS") 
saveRDS(TSI_81432306005, file = "TSI_81432306005.RDS") 












