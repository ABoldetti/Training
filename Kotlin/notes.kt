import kotlin.properties.ReadWriteProperty
import kotlin.reflect.KProperty


/**
 * You can edit, run, and share this code.
 * play.kotlinlang.org
 */
//-----------------------------------------------------------------------------------------------
//Classes
open class SmartDevice (var name:String , var category:String){
    
    var device_status:String = "off"
    open var volume:Int = 50
    	set(new_volume: Int){
            when(new_volume){
                in 0..100 -> field = new_volume
                else -> println("volume unacceptable")
            }
        }
        
    constructor( name:String , category:String , status:Int):this(name,category){
        device_status = when(status){
            0 -> "off"
            1 -> "on"
            else ->"boh"
        }
    }
    
    open fun turnOn(){
        println("Device is Turned On xoxo")
    }
    open fun turnOff(){
        println("Device is Turned Off (cazzo di sogliola)")
        println("$device_status")
    }
}
//-----------------------------------------------------------------------------------------------

//Is-A relationship between classes
class SmartTV(deviceName:String , deviceCategory:String):
	SmartDevice( name = deviceName , category = deviceCategory){
    
        override var volume by RangeReader( initialValue=0 , minValue=0 , maxValue = 100)
        var channelNumber:Int = 100
        	set(new_channel){ if ( new_channel in 100..1000) field = new_channel}
        
        fun increaseVolume(){
            volume++
        	println( "$volume")
        }
        
        override fun turnOn(){
            super.turnOn()
        }
}
//-----------------------------------------------------------------------------------------------
//Has-A relationship between classes
class Toaster( val SmartDevice:SmartDevice){
    //non ho voglia di scrivere
}
//-----------------------------------------------------------------------------------------------
//Delegates, this shit is hardcore
class RangeReader(
	initialValue: Int,
    private val minValue: Int,
    private val maxValue: Int
	):ReadWriteProperty<Any?,Int>{
    
    var fieldData = initialValue
    
    override fun getValue( thisRef: Any? , property:KProperty<*>): Int {
        return fieldData
        
    }
    override fun setValue( thisRef: Any? , property:KProperty<*> , value : Int) {
        if( value in minValue..maxValue) fieldData = value
    }
}
//-----------------------------------------------------------------------------------------------
fun main() {
    val a: String = "Aaa"
    var smartDevice = SmartDevice("SmartTV" , "ent",1)
    smartDevice.turnOff()
    
    when( a ){
        //"diocane","ziocane" -> println("cane")
        "madonna" -> println("cagna")
        in "z" .. "ziocane" -> println("cazzo fai")
        is String? -> println("wtf")
        else -> println("coglione")
    }
    
    
}
//function as variables
var trick:()->Unit = {
    println("no sweet")
}

val treat:()->Unit = {
    println("sweet")
}


fun trickOrTreat( A:Boolean , trick:()->Unit , treat:()->Unit):()->Unit{
    when(A){
        true -> return treat
        false -> return trick
    }
}
//------------------------------------------------------------------------------------------
//compact functions
val coins: (Int) -> String = { quantity ->
        "$quantity quarters"
    }
    val coins_better: (Int) -> String = {
        "$it quarters"
    }

