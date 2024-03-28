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
            <RouterLink to="/home" custom v-slot="{isActive, href, navigate}">
              <NavigationMenuLink as-child :active="isActive">
                <a :href="href" @click="navigate">Accueil</a>
              </NavigationMenuLink>
            </RouterLink>
          </NavigationMenuItem>
          <NavigationMenuItem>
            <RouterLink to="/exercices" custom v-slot="{isActive, href, navigate}">
              <NavigationMenuLink as-child :active="isActive">
                <a :href="href" @click="navigate">Exercices</a>
              </NavigationMenuLink>
            </RouterLink>
          </NavigationMenuItem>
          <NavigationMenuItem>
            <RouterLink to="/users" custom v-slot="{isActive, href, navigate}">
              <NavigationMenuLink as-child :active="isActive">
                <a :href="href" @click="navigate">Utilisateurs</a>
              </NavigationMenuLink>
            </RouterLink>
          </NavigationMenuItem>
        </NavigationMenuList>
      </NavigationMenu>

    </div>
  </header>

  <RouterView />
</template>
