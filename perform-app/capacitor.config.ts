import type { CapacitorConfig } from '@capacitor/cli';

const config: CapacitorConfig = {
  appId: 'perform.app',
  appName: 'Perform',
  webDir: 'dist',
  cordova: {
    preferences: {
      Orientation: 'portrait'
    }
  }
};

export default config;
