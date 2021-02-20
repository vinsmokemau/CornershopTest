<template lang="html">
  <div>
    <b-navbar type="dark" variant="dark">
      <b-navbar-nav>
        <b-nav-item href="/">Home</b-nav-item>
      </b-navbar-nav>
    </b-navbar>
    
    <div class="container">
      
      <div class="row">
        <div class="col text-left">
          <h2>Menu for {{ day }}</h2>
        </div>
      </div>

      <div class="row">
        <div class="col">
          <div class="card">
            <div class="card-body">
              
              <form @submit="onSubmit">

                <div class="form-group row">
                  <label for="orders" class="col-sm-2 col-form-label">
                    Options:
                  </label>
                  <div class="col-sm-6">
                    <select 
                      name="orders"
                      class="form-control"
                      v-model.trim="form.option"
                    >
                      <option v-for="option in options" v-bind:value="option.id">
                        {{ option.description }}
                      </option>
                    </select>
                  </div>
                </div>

                <div class="form-group row">
                  <label for="specifications" class="col-sm-2 col-form-label">Specifications</label>
                  <div class="col-sm-6">
                    <input type="text" name="specifications" class="form-control" v-model.trim="form.specifications">
                  </div>
                </div>

                <div class="rows">
                  <div class="col text-left">
                    <b-button type="submit" variant="success">Order</b-button>
                  </div>
                </div>

              </form>

            </div>
          </div>
        </div>
      </div>
    
    </div>

  </div>
</template>

<script>

import axios from 'axios';
import swal from 'sweetalert';

export default {
  data () {
    return {
      day: '',
      options: [],
      specifications: '',
      form: {
        user: Number(this.$route.params.idUser),
        option: '',
        specifications: '',
      }
    }
  },
  methods: {

    getMenu () {
      const path = `http://0.0.0.0:8000/menu/`

      axios.get(path).then((response) => {
        this.day = response.data.day
        this.options = response.data.options
      })
      .catch((error) => {
        console.log(this.form)
      })
    },

    onSubmit(evt) {
      evt.preventDefault()
      
      const path = `http://0.0.0.0:8000/orders/`

      axios.post(path, this.form).then((response) => {
        this.form.user = response.data.user
        this.form.option = response.data.option
        this.form.specifications = response.data.specifications
        swal("Order registered", "", "success")
      })
      .catch((error) => {
        console.log(error)
        swal("Ooops", "A problem ocurrs", "error")
      })
    },
  },

  created() {
    this.getMenu()
  },

}
</script>

<style lang="css" scoped>
</style>