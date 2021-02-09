<!DOCTYPE html>
<html lang="eng">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Asal Sayi</title>
    
</head>
<body>
    <div>
    <h1>Asal Sayi</h1>

        
        <form>
            <label>Sayiyi giriniz:</label>
            <input type="number" id="fname" name="sayi" value="Sayiyi Giriniz"><br><br>
            <input type="submit" value="Bu sayi asal sayi mi?">
        </form><br>
            <?php 
                
                $degisken = $_GET["sayi"];

                $asal=0; $i=2;
 
                do
                {
                    if ($degisken % $i == 0)
                    {
                        $asal = 1;
                    }
                    $i++;
                }
                while($i<$degisken);
                 
                if ($asal != 1)
                {
                    $sonuc="Bu sayi asal sayidir";
                }
                else if ($degisken == 2)
                {
                    $sonuc="Bu sayı asal sayidir";
                }
                else 
                {
                    $sonuc="Bu sayı asal sayi degildir"; 
                }

                echo $degisken;
                echo $sonuc;
                ?>
                
                
                    
            
     </div>

    </body>
</html>
