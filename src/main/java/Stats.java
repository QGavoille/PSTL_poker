import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.HashMap;

public class Stats {


    public static void main(String[] args) throws IOException {
        for(int i = 0; i<52; i++){
            System.out.println(i);
            File f = new File("test/eta"+i+".test");
          
            FileWriter fw = new FileWriter(f.getAbsoluteFile());
            BufferedWriter bw = new BufferedWriter(fw);

            HashMap<Integer,Integer> posOcc = new HashMap<>();
            for(int tmp = 0; tmp<52;tmp++){
                posOcc.put(tmp,0);
            }
            for(int k = 0; k<1000000;k++){
                Partie p = new Partie();

               
                CardGame pack = p.getDeck();
                for(int k2 = 0; k2<52;k2++){
                    if(pack.getDeck()[k2].toInt()== i){
                    
                        posOcc.put(k2,posOcc.get(k2)+1);
                    }
                }

            }
            String towrite = "";
            for(Integer k :posOcc.keySet() ){
            	
                towrite+=("\n"+k+"//"+posOcc.get(k));
                
            }
            
            
            bw.write(towrite);
            bw.close();
 
        }
       




    }
}
