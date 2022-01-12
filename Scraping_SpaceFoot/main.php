<?php

$db=new PDO("mysql:host=192.168.64.2;dbname=SpaceFoot;","Louka","Louka");

$linesTitre = file("titre.txt");
$linesContrat = file("typeDeContrat.txt");
$linesTeam = file("team.txt");
$linesLocalisation = file("localisation.txt");
$linesDate = file("datePublication.txt");
$linesContenu = file("contenu.txt");


$req = 'INSERT INTO Site (titre, contrat, team, localisation, date, contenu)
VALUES (:titre , :contrat, :team, :localisation, :date, :contenu)';

for($i = 0; $i <= 18; $i++){


    $stm = $db->prepare($req);
    
    $titre = $linesTitre[$i];
    $contrat = $linesContrat[$i];
    $team = $linesTeam[$i];
    $localisation = $linesLocalisation[$i];
    $date = $linesDate[$i];
    $contenu = $linesContenu[$i];
    

    $stm->execute([':titre'=>$titre , ':contrat'=>$contrat, ':team'=>$team, ':localisation'=>$localisation, ':date'=>$date, ':contenu'=>$contenu]);

}

        // ----------------   Requete pour compter le nombre d'offre par Team -------------- //

$query = $db->prepare('SELECT team, COUNT(contrat) AS "Nombre de contrat possible"  
FROM `Site` 
GROUP BY team; ');

$query->execute();

$results = $query->fetchAll(PDO::FETCH_ASSOC);



function download_csv_results($results)
{            
    $outstream = fopen("test.csv", "w");    
    fputcsv($outstream, array_keys($results[0]));

    foreach($results as $result)
    {
        fputcsv($outstream, $result);
    }

    fclose($outstream);
}
download_csv_results($results); 