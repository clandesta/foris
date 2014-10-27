import java.util.ArrayList;
import java.util.List;

public class MEIN {
      
      public static void main(String[] args) {
            //StringBuilder builder=new StringBuilder(cadena);
            String texto2 = "afoolishconsistencyisthehobgoblinoflittlemindsadoredbylittlestatesmenandphilosophersanddivineswithconsistencyagreatsoulhassimplynothingtodohemayaswellconcernhimselfwithhisshadowonthewallspeakwhatyouthinknowinhardwordsandtomorrowspeakwhattomorrowthinksinhardwordsagainthoughitcontradicteverythingyousaidtodayahsoyoushallbesuretobemisunderstoodisitsobadthentobemisunderstoodpythagoraswasmisunderstoodandsocratesandjesusandlutherandcopernicusandgalileoandnewtonandeverypureandwisespiritthatevertookfleshtobegreatistobemisunderstood";
                  
            //chilean güey String tex = "laputaanitalavalatinaconsapolio";
            //chilean güey String tex2 = "somosseresanitalavalatinalarutanosaportootropasonaturallamoralclaromalamanapanama";
            
            long inicio = System.currentTimeMillis();
            
            List<String> encontrados = new ArrayList<String>();
            
            for(int i=0;i<texto2.length();i++){
                  char letraIni = texto2.charAt(i);
                  for(int a = i+1; a<texto2.length();a++){
                        if(letraIni == texto2.charAt(a)){
                             String strEncontrado = texto2.substring(i, a+1);
                             if((a-i) >1 && invertirCadena(strEncontrado).equals(strEncontrado)){
                                   encontrados.add(strEncontrado);
                                         System.out.println("Match: " + strEncontrado);
                             }
                        }
                  }
            }
            
            //Buscar mayor
            int max = 0;
            for(int e =1; e<encontrados.size();e++){
                  
                  if(encontrados.get(e).length()>encontrados.get(max).length()){
                        max = e;
                  }
            }
            String masLargo = encontrados.get(max);
            System.out.println("Palídnromo más largo: " + masLargo+ ", largo: " + masLargo.length());
            
            long termino = System.currentTimeMillis()-inicio;
            System.out.println("Tiempo " + termino + " ms");

            
      }
      
      private static String invertirCadena(String in){
            String out = "";
            for(int i=in.length()-1;i>=0;i--){
                  out += in.charAt(i);
            }
            return out;
      }
}
