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
          <h2>Create Menu</h2>
        </div>
      </div>

      <div class="row">
        <div class="col">
          <div class="card">
            <div class="card-body">
              
              <form @submit="onSubmit">

                <div class="form-group row">
                  <label for="day" class="col-sm-2 col-form-label">Day</label>
                  <div class="col-sm-6">
                    <input type="date" name="day" class="form-control" v-model.trim="form.day">
                  </div>
                </div>

                <hr>

                <h4>Options</h4>

                <div class="form-group row">
                  <label for="options0" class="col-sm-2 col-form-label">Option 1</label>
                  <div class="col-sm-6">
                    <input type="text" placeholder="Ej: Corn pie, Salad and Dessert" name="options0" class="form-control" v-model.trim="form.options[0].description">
                  </div>
                </div>

                <div class="form-group row">
                  <label for="options1" class="col-sm-2 col-form-label">Option 2</label>
                  <div class="col-sm-6">
                    <input type="text" placeholder="Ej: Chicken Nugget Rice, Salad and Dessert" name="options1" class="form-control" v-model.trim="form.options[1].description">
                  </div>
                </div>

                <div class="form-group row">
                  <label for="options2" class="col-sm-2 col-form-label">Option 3</label>
                  <div class="col-sm-6">
                    <input type="text" placeholder="Ej: Rice with hamburger, Salad and Dessert" name="options2" class="form-control" v-model.trim="form.options[2].description">
                  </div>
                </div>

                <div class="form-group row">
                  <label for="options3" class="col-sm-2 col-form-label">Option 4</label>
                  <div class="col-sm-6">
                    <input type="text" placeholder="Ej: Premium chicken Salad and Dessert" name="options3" class="form-control" v-model.trim="form.options[3].description">
                  </div>
                </div>

                <div class="rows">
                  <div class="col text-left">
                    <b-button type="submit" variant="success">Create</b-button>
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
      form: {
        day: '',
        options: [
          {description: ''},
          {description: ''},
          {description: ''},
          {description: ''},
        ],
      },
    }
  },
  methods: {

    onSubmit (evt) {

      evt.preventDefault()
      
      const path = `http://0.0.0.0:8000/menus/`
      
      axios.post(path, this.form).then((response) => {
        this.form.day = response.data.day
        this.form.options = response.data.options
        swal("Menu creation succesfull!", "", "success")
      })
      .catch((error) => {
        console.log(error)
        swal("Ooops!", "A problem ocurrs", "error")
      })
    },
  },
}
</script>

<style lang="css" scoped>
</style>