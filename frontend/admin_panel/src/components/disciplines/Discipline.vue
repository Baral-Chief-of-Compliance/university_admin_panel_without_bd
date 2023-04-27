<template>
    <div class="text-center">
        <v-dialog
            v-model="dialog"
            width="auto"
        >
            <template v-slot:activator="{ props }">
                <div class="text-h3 py-6 mx-10 text-left">{{ name_dis }}</div>

               
                <v-container class="d-flex justify-center">
                    <v-col>
                        <v-row class="mx-10">
                            <v-col  v-for="f in forms_of_work" :key="f.num_work" cols="12" md="3"  v-bind="props_hover">
                                <v-hover v-slot="{ isHovering, props }" >
                                    <v-card  class="mx-auto" height="200" width="300" 
                                        v-bind="props"
                                        :color="isHovering ? 'indigo': undefined"
                                    >
                                        <v-card-item class="text-h6">
                                            {{ f.name_control }}
                                        </v-card-item>
                                    </v-card>

                                    <v-card-actions class="mt-3">
                                        <v-spacer></v-spacer>
                                        <v-btn @click="delete_work(f)" variant="outlined" color="red"
                                        >Удалить</v-btn>
                                    </v-card-actions>
                                </v-hover>
                            </v-col>
                        </v-row>    
                        <v-row class="mx-14 mt-15">
                            <v-btn  block
                                color="indigo"
                                v-bind="props"
                            >
                                Добавить форму контроля
                                </v-btn>
                        </v-row>

                    </v-col>
                </v-container>
            </template>

            <v-card>
                <v-card-title>
                    Форма добавления для формы контроля
                </v-card-title>
                <v-form>
                    <v-text-field
                        v-model="name_control"
                        label="Название"
                        color="indigo"
                        class="mx-5 mb-5"
                    >
                    </v-text-field>

                </v-form>
                <v-card-actions>
                    <v-btn color="red"  @click="dialog = false">Закрыть</v-btn>
                    <v-btn color="green"  @click="add_forms_of_work">Добавить</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>    
    </div>
</template>
<script>
import axios from "axios"
import json from '@/data/disciplines.json'


export default{
    data: () => ({
        disciplines: json,
        name_dis: "",
        forms_of_work: [],
        dialog: false,
        name_control: "",
        num_dis: ""
    }),

    mounted(){
        this.get_inf_discipline()
    },

    updated(){
        this.get_inf_discipline()
    },

    methods: {
        get_inf_discipline(){
            let discipline = this.disciplines.find(item => item.num_dis == this.$route.params.num_dis)
            this.name_dis = discipline.name_dis
            this.forms_of_work = discipline.forms_of_work,
            this.num_dis = discipline.num_dis
        },

        add_forms_of_work(){
            let num_work = this.forms_of_work.length + 1
            this.forms_of_work.push({
                "name_control": this.name_control,
                "num_dis": this.num_dis,
                "num_work": num_work
            })

            axios.post("http://127.0.0.1:5000/disciplines", {
                disciplines: this.disciplines
            })

            this.name_control = ""
            this.dialog = false
        },

        delete_work(f){
            for (let i=0; i<this.forms_of_work.length; i++){
                if (this.forms_of_work[i] == f){
                    this.forms_of_work.splice(i,1)
                }
            }

            axios.post("http://127.0.0.1:5000/disciplines", {
                disciplines: this.disciplines
            })
        }

    }
}
</script>