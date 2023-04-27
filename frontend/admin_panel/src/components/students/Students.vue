<template>
    <div class="text-center">
        <v-dialog
            v-model="dialog"
            width="auto"
        >
            <template v-slot:activator="{ props }">
                <div class="text-h3 py-6 mx-10 text-left">Студенты</div>

               
                <div class="py-6 mx-10 d-flex justify-center" >
                    <v-col>
                        <div v-for="s in students">
                            <v-hover v-slot="{ isHovering, props }" >
                                <v-card  class="my-2 pa-6 mx-14 d-flex flex-row"
                                    v-bind="props"
                                    :color="isHovering ? 'indigo': undefined"
                                    :to="{ name: 'student', params: {num_credit: s.num_credit}}"
                                >
                                    <b class="pr-2">Фамилия:</b>  {{ s.surname_s }} 
                                    <v-spacer></v-spacer> 
                                    <b class="pr-2">Имя:</b> 
                                    {{ s.name_s }} 
                                    <v-spacer></v-spacer> 
                                    <b class="pr-2">Отчество:</b>  
                                    {{ s.patro_s }} 
                                    <v-spacer></v-spacer> 
                                    <b class="pr-2">Группа:</b>
                                    {{ s.num_group  }}
                                    <v-spacer></v-spacer>
                                    <b class="pr-2">Номер зачетки:</b>
                                    {{ s.num_credit  }}

                                </v-card>

                                <v-card-actions class="mt-3">
                                    <v-spacer></v-spacer>
                                    <v-btn @click="delete_student(s)" variant="outlined" color="red"
                                    >Удалить</v-btn>
                                </v-card-actions>
                            </v-hover>
                        </div>
                        <div class="my-2 pt-6 mx-14 d-flex flex-row">
                            <v-btn  block
                                color="indigo"
                                v-bind="props"
                            >
                                Добавить студента
                                </v-btn>
                        </div>

                    </v-col>
                </div>
            </template>

            <v-card>
                <v-card-title>
                    Форма для добавления студента
                </v-card-title>
                <v-form>
                    <v-text-field
                        v-model="surname_s"
                        label="Фамилия"
                        color="indigo"
                        class="mx-5 mb-1"
                    >
                    </v-text-field>

                    <v-text-field
                        v-model="name_s"
                        label="Имя"
                        color="indigo"
                        class="mx-5 mb-1"
                    >
                    </v-text-field>

                    <v-text-field
                        v-model="patro_s"
                        label="Отчество"
                        color="indigo"
                        class="mx-5 mb-1"
                    >
                    </v-text-field>

                    <v-text-field
                        v-model="num_group"
                        label="Группа"
                        color="indigo"
                        class="mx-5 mb-1"
                    >
                    </v-text-field>

                    <v-text-field
                        v-model="year_of_admission"
                        label="Год поступления"
                        color="indigo"
                        class="mx-5 mb-1"
                    >
                    </v-text-field>

                    <v-text-field
                        v-model="num_credit"
                        label="Номер зачетки"
                        color="indigo"
                        class="mx-5 mb-1"
                    >
                    </v-text-field>
                </v-form>
                <v-card-actions>
                    <v-btn color="red"  @click="dialog = false">Закрыть</v-btn>
                    <v-btn color="green"  @click="add_student">Добавить</v-btn>
                </v-card-actions>
            </v-card>
        </v-dialog>    
    </div>
</template>
<script>
import axios from "axios"
import json from '@/data/students.json'


export default{
    data: () => ({
        students: json,
        dialog: false,
        surname_s: "",
        name_s: "",
        patro_s: "",
        num_group: "",
        year_of_admission: "",
        num_credit: "",
    }),

    // mounted(){
    //     this.get_studnets()
    // },

    // updated(){
    //     this.get_studnets()
    // },

    methods: {


        add_student(){

            this.students.push({
                "name_s": this.name_s,
                "num_credit": this.num_credit,
                "num_group": this.num_group,
                "patro_s": this.patro_s,
                "surname_s": this.surname_s,
                "year_of_admission": this.year_of_admission,
                "delivery": []
            })

            axios.post("http://127.0.0.1:5000/students", {
                students: this.students
            })
            
            this.surname_s = ""
            this.name_s = ""
            this.patro_s = ""
            this.num_group = ""
            this.year_of_admission = ""
            this.num_credit = ""

            this.dialog = false
        },
        delete_student(s){
            for (let i=0; i<this.students.length; i++){
                if (this.students[i] == s){
                    this.students.splice(i,1)
                }
            }

            axios.post("http://127.0.0.1:5000/students", {
                students: this.students
            })
        }
    }
}
</script>