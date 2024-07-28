library(data.table)
dt <- data.table(id = 1:1e6, value = rnorm(1e6))
dt_summary <- dt[, .(mean_value = mean(value)), by = id]
