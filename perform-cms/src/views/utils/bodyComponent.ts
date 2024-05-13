const setMuscleSelected = (key: string, action: string, muscle_selected : any) => {
    if (action === 'add') {
      const findKey =
        muscle_selected.filter(function (element : any) {
          return element === key
        }).length == 0
      console.log(findKey)
      if (findKey) {
        muscle_selected.push(key)
      }
    } else {
      // Trouver l'index de la valeur à supprimer
      const index = muscle_selected.indexOf(key)
  
      if (index !== -1) {
        // Supprimer la valeur à l'index trouvé
        muscle_selected.splice(index, 1)
      }
    }
  }

export default { setMuscleSelected }