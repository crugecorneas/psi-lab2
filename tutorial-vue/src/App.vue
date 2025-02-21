<!-- App.vue -->
<template>
  <div id="app" class="container">
    <div class="row">
      <div class="col-md-12">
        <h1>Personas</h1>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12">
        <!-- Inclusion del componente "TablaPersonas" -->
        <formulario-persona @add-persona="agregarPersona" />
        <tabla-personas :personas="personas" />
      </div>
    </div>
  </div>
</template>

<script setup>
// Importacion del componente 'TablaPersonas' y el metodo 'ref' de Vue 3
import TablaPersonas from '@/components/TablaPersonas.vue'
import FormularioPersona from '@/components/FormularioPersona.vue'
import { ref } from 'vue';
// Definicion del componente Vue
defineOptions({
  // Nombre del componente
  name: 'app',
});
// Declaracion de una variable reactiva "personas" usando "ref"
const personas = ref([
]);

const agregarPersona = (persona) => {
  let id = 0;
  if (personas.value.length > 0) {
    id = personas.value[personas.value.length - 1].id + 1;
  }
  personas.value = [...personas.value, { ...persona, id }];
};
</script>

<style>
/* Estilos globales para todos los elementos button en la aplicacion */
button {
  background: #009435;
  border: 1px solid #009435;
}
</style>
<style>
/* Estilos globales para todos los elementos button en la aplicacion */
button {
  background: #009435;
  border: 1px solid #009435;
}
</style>