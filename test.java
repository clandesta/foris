public class test{

public static void main(String[] args){
    // for (int i=0;i<999 ;i++) {
    //     System.out.println(i);
    //     System.out.println(cortarCampos(""+i, 2, "0"));
    //     System.out.println("------------------------------------");
    // }
    System.out.print( formatCampos("1",5 ));
    String var = formatCampos("holanda",10) + formatCampos("125",20) + formatCampos("holanda",20);
    System.out.println(var);

}

public static String formatCampos(String txt, int largo){
    try {
        //Formatear con 0 a la izquierda
        return String.format("%0"+String.valueOf(largo)+"d" ,Integer.parseInt(txt));
    } catch (NumberFormatException e) {
        //es String llenar con espacios a la derecha
         return String.format("%1$-" + largo + "s", txt);
    }
}

public static String cortarCampos(String campo, int largo, String caracter) {

    if (campo.length() <= largo) {
        return campo;
    }

    if (caracter.equals("0")) {
        
        //cortar cadena de numeros desde derecha a izquierda
        //ej: 001000000, con largo 7
        //campo.substring(9-7=2,7) ->1000000
        return campo.substring(campo.length() - largo, campo.length());
    } else {
        return campo.substring(0, largo);
    }
  }
  
}