fun main() {
    // Fill in the code.
    
}


fun printFinalTemperature(
    initialMeasurement: Double, 
    initialUnit: String, 
    finalUnit: String, 
    conversionFormula: (Double) -> Double
) {
    val finalMeasurement = String.format("%.2f", conversionFormula(initialMeasurement)) // two decimal places
    println("$initialMeasurement degrees $initialUnit is $finalMeasurement degrees $finalUnit.")
}

val celsiusToFahrenheit:( Double ) -> Double = { ((9.0/5.0)*it) + 32 }
val kelvinToCelsius:( Double ) -> Double = { it - 273.15}
val fahrenheitToKelvin( Double ) -> Double = { (it-32.0)*(5.0/9) + 273.15}