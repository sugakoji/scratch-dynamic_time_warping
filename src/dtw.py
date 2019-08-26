# 気をつける点
# https://medium.com/@shachiakyaagba_41915/dynamic-time-warping-with-time-series-1f5c05fb8950


def get_dtw_distance(x_vec, y_vec):
    
    x_length = len(x_vec) +1
    y_length = len(y_vec)+1 

    dtw_dis = np.full((x_length,y_length), np.inf)
    dtw_dis[0][0] = 0
    for i in range(1, x_length):
        for j in range(1, y_length):
            base_dis = abs(sin_wave[i-1] -  cos_wave[j-1])
            dtw_dis[i][j] = base_dis + min(dtw_dis[i-1][j-1],
                                           dtw_dis[i-1][j],
                                           dtw_dis[i][j-1])
    return dtw_dis[-1][-1]
