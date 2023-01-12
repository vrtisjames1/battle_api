from rest_framework import serializers 
from .models import Games

class GamesSerializer(serializers.ModelSerializer): # serializers.ModelSerializer just tells django to convert sql to JSON
    class Meta:
        model = Games # tell django which model to use
        fields = ('id','game_name','winner', 'username1', 'user1_turn', 'username2', 'user2_turn',
        'a1','a2','a3','a4','a5','a6','a7','a8','a9','a10',
        'b1','b2','b3','b4','b5','b6','b7','b8','b9','b10',
        'c1','c2','c3','c4','c5','c6','c7','c8','c9','c10',
        'd1','d2','d3','d4','d5','d6','d7','d8','d9','d10',
        'e1','e2','e3','e4','e5','e6','e7','e8','e9','e10',
        'f1','f2','f3','f4','f5','f6','f7','f8','f9','f10',
        'g1','g2','g3','g4','g5','g6','g7','g8','g9','g10',
        'h1','h2','h3','h4','h5','h6','h7','h8','h9','h10',
        'i1','i2','i3','i4','i5','i6','i7','i8','i9','i10',
        'j1','j2','j3','j4','j5','j6','j7','j8','j9','j10',
        'a1_2','a2_2','a3_2','a4_2','a5_2','a6_2','a7_2','a8_2','a9_2','a10_2',
        'b1_2','b2_2','b3_2','b4_2','b5_2','b6_2','b7_2','b8_2','b9_2','b10_2',
        'c1_2','c2_2','c3_2','c4_2','c5_2','c6_2','c7_2','c8_2','c9_2','c10_2',
        'd1_2','d2_2','d3_2','d4_2','d5_2','d6_2','d7_2','d8_2','d9_2','d10_2',
        'e1_2','e2_2','e3_2','e4_2','e5_2','e6_2','e7_2','e8_2','e9_2','e10_2',
        'f1_2','f2_2','f3_2','f4_2','f5_2','f6_2','f7_2','f8_2','f9_2','f10_2',
        'g1_2','g2_2','g3_2','g4_2','g5_2','g6_2','g7_2','g8_2','g9_2','g10_2',
        'h1_2','h2_2','h3_2','h4_2','h5_2','h6_2','h7_2','h8_2','h9_2','h10_2',
        'i1_2','i2_2','i3_2','i4_2','i5_2','i6_2','i7_2','i8_2','i9_2','i10_2',
        'j1_2','j2_2','j3_2','j4_2','j5_2','j6_2','j7_2','j8_2','j9_2','j10_2',
        'stat_a1','stat_a2','stat_a3','stat_a4','stat_a5','stat_a6','stat_a7','stat_a8','stat_a9','stat_a10',
        'stat_b1','stat_b2','stat_b3','stat_b4','stat_b5','stat_b6','stat_b7','stat_b8','stat_b9','stat_b10',
        'stat_c1','stat_c2','stat_c3','stat_c4','stat_c5','stat_c6','stat_c7','stat_c8','stat_c9','stat_c10',
        'stat_d1','stat_d2','stat_d3','stat_d4','stat_d5','stat_d6','stat_d7','stat_d8','stat_d9','stat_d10',
        'stat_e1','stat_e2','stat_e3','stat_e4','stat_e5','stat_e6','stat_e7','stat_e8','stat_e9','stat_e10',
        'stat_f1','stat_f2','stat_f3','stat_f4','stat_f5','stat_f6','stat_f7','stat_f8','stat_f9','stat_f10',
        'stat_g1','stat_g2','stat_g3','stat_g4','stat_g5','stat_g6','stat_g7','stat_g8','stat_g9','stat_g10',
        'stat_h1','stat_h2','stat_h3','stat_h4','stat_h5','stat_h6','stat_h7','stat_h8','stat_h9','stat_h10',
        'stat_i1','stat_i2','stat_i3','stat_i4','stat_i5','stat_i6','stat_i7','stat_i8','stat_i9','stat_i10',
        'stat_j1','stat_j2','stat_j3','stat_j4','stat_j5','stat_j6','stat_j7','stat_j8','stat_j9','stat_j10',) 