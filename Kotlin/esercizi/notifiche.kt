fun main() {
    val morningNotification = 51
    val eveningNotification = 135
    
    printNotificationSummary(morningNotification)
    printNotificationSummary(eveningNotification)
}


fun printNotificationSummary(numberOfMessages: Int) {
    // Fill in the code.
    when ( numberOfMessages){
        0 -> println("you have no notifications")
        1 -> println("you have 1 notification")
        in 2..99 -> println("you have $numberOfMessages notifications")
        else -> println("you have +99 notifications")
    }
}