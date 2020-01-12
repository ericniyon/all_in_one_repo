<template>
  <div>
      <h2> {{title}} </h2>
    <slot></slot>
  </div>
</template>

<script>
export default {
  
  data () {
    return {
      title:'Hey Am The form Helper'
    }
  }
}
</script>

<style>

</style>
