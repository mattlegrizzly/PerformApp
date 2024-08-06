import { onMounted, onBeforeUnmount } from 'vue';
import { Keyboard } from '@capacitor/keyboard';
import { Capacitor } from '@capacitor/core';

export function useKeyboardControl() {
  const handleClickOutside = (event) => {
    if (!event.target.closest('.native-input, ion-textarea') && document.activeElement) {
      document.activeElement.blur(); // Ferme le clavier
    }
  };

  const handleKeyboardDidHide = () => {
    document.activeElement?.blur(); // Ferme le clavier
  };

  onMounted(() => {
    document.addEventListener('click', handleClickOutside);
    if (Capacitor.isNativePlatform()) {
      Keyboard.addListener('keyboardDidHide', handleKeyboardDidHide);
    }
  });

  onBeforeUnmount(() => {
    document.removeEventListener('click', handleClickOutside);
    if (Capacitor.isNativePlatform()) {
      Keyboard.removeAllListeners(); // Nettoyer les listeners
    }
  });
}
