<script setup lang="ts">
import { RouterLink, RouterView } from 'vue-router'
import {
  NavigationMenu,
  NavigationMenuItem,
  NavigationMenuLink,
  NavigationMenuList,
} from '@/components/ui/navigation-menu'
</script>

<template>
  <header>

    <div class="wrapper">
      <NavigationMenu>
        <NavigationMenuList>
          <NavigationMenuItem>
            <RouterLink to="/" custom v-slot="{isActive, href, navigate}">
              <NavigationMenuLink as-child :active="isActive">
                <a :href="href" @click="navigate">home</a>
              </NavigationMenuLink>
            </RouterLink>
          </NavigationMenuItem>
          <NavigationMenuItem>
            <RouterLink to="/second" custom v-slot="{isActive, href, navigate}">
              <NavigationMenuLink as-child :active="isActive">
                <a :href="href" @click="navigate">second</a>
              </NavigationMenuLink>
            </RouterLink>
          </NavigationMenuItem>
        </NavigationMenuList>
      </NavigationMenu>

    </div>
  </header>

  <RouterView />
</template>
