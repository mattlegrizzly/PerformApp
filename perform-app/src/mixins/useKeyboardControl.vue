// src/composables/useKeyboardControl.js
import { onMounted, onBeforeUnmount } from 'vue';
import { Keyboard } from '@capacitor/keyboard';

export function useKeyboardControl() {
  const handleClickOutside = (event) => {
    if (!event.target.closest('ion-input, ion-textarea')) {
      console.log('ferme le clavier')
      document.activeElement.blur(); // Ferme le clavier
    }
  };

  const handleKeyboardDidHide = () => {
    document.activeElement.blur(); // Ferme le clavier
  };

  onMounted(() => {
    document.addEventListener('click', handleClickOutside);
    Keyboard.addListener('keyboardDidHide', handleKeyboardDidHide);
  });

  onBeforeUnmount(() => {
    document.removeEventListener('click', handleClickOutside);
    Keyboard.removeAllListeners(); // Nettoyer les listeners
  });
}
