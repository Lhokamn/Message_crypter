


function copierPressePapier() {
    /**
     * Permet de copier le contenu dans la textarea.
     * 
     * Précision, on récupère les éléments avec les classes et non les ID car il n'y en a qu'un seul de chaque.
     */

    // Permet de sélectioner la textArea
    let editor = document.querySelector('textarea');

    //Permet de sélectionnet le bouton
    //let button = document.querySelector('button');
    let button = document.getElementById('boutonCopier');

    //Permet de détecter le click sur le bouton
    button.addEventListener('click', () => {
        console.log("click");
            // Permet de sélectionner tout le texte
            editor.select();

            // Copy le texte présent dans la textbox
            document.execCommand('copy');

            // On change ce qu'affiche le bouton 
            button.innerText= "Copié";
    });
}

copierPressePapier();