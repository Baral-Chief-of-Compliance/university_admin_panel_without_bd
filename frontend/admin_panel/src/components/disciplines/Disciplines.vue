<template>
    <div class="text-center">
        <v-dialog
            v-model="dialog"
            width="auto"
        >
            <template v-slot:activator="{ props }">
                <div class="text-h3 py-6 mx-10 text-left">Дисциплины</div>

               
                <v-container class="d-flex justify-center">
                    <v-col>
                        <v-row class="mx-10">
                            <v-col  v-for="d in disciplines" :key="d.num_dis" cols="12" md="3"  v-bind="props_hover">
                                <v-hover v-slot="{ isHovering, props }" >
                                    <v-card  class="mx-auto" height="200" width="300" 
                                        v-bind="props"
                                        :color="isHovering ? 'indigo': undefined"
                                        :to="{ name: 'discipline', params: {num_dis: d.num_dis}}"
                                    >
                                        <v-card-item class="text-h6">
                                            {{ d.name_dis }}
                                        </v-card-item>
                                    </v-card>

                                    <v-card-actions class="mt-3">
                                        <v-spacer></v-spacer>
                                        <v-btn @click="delete_discipline(d)" variant="outlined" color="red"
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
                                Добавить дисциплину
                                </v-btn>
                        </v-row>

                    </v-col>
                </v-container>
            </template>

            <v-card>
                <v-card-title>
                    Форма для добавления дисциплины
                </v-card-title>
                <v-form>
                    <v-text-field
                        v-model="name_dis"
                        label="Название"
                        color="indigo"
                        class="mx-5 mb-5"
                    >
                    </v-text-field>

                </v-form>
                <v-card-actions>
                    <v-btn color="red"  @click="dialog = false">Закрыть</v-btn>
                    <v-btn color="green"  @click="add_discipline">Добавить</v-btn>
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
        dialog: false,
        name_dis: ""
    }),

    // mounted(){
    //     this.get_disciplines()
    // },

    // updated(){
    //     this.get_disciplines()
    // },

    methods: {

        add_discipline(){
            let num_dis = this.disciplines.length + 1
            
            this.disciplines.push({
                "num_dis": num_dis,
                "name_dis": this.name_dis,
                "forms_of_work":[]
            })

            axios.post("http://127.0.0.1:5000/disciplines", {
                disciplines: this.disciplines
            })
            
            this.name_dis = ""

            this.dialog = false
        },

        delete_discipline(d){
            for (let i=0; i<this.disciplines.length; i++){
                if(this.disciplines[i] == d){
                    this.disciplines.splice(i,1)
                }
            }

            axios.post("http://127.0.0.1:5000/disciplines", {
                disciplines: this.disciplines
            })
        }

    }
}
</script>