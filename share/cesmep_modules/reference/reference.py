def variable2reference(variable, project=None, my_obs={}) :
  if variable in my_obs:
       tmpdict = dict(variable=variable)
       tmpdict.update(my_obs[variable])
       return tmpdict
  else:
    if not project:
        if variable in ['pr','prw','rlut', 'rsut' , 'rlutcs', 'rsutcs', 'rlus', 'rsus' , 'rluscs', 'rsuscs', 'rlds', 'rsds',
                        'rsdscs','rldscs','tas', 'ta', 'ua', 'va', 'psl', 'uas', 'vas', 'tos', 'sos', 'zos','hus','hur','mlotst','alb',
                        'thetao','to','so','so200','so1000','so2000','to200','to1000','to2000','sic','wfo','hurs','huss',
                        'cltcalipso','clhcalipso','clmcalipso','cllcalipso','hfls','hfss','tauu','tauv','tauuo','tauvo',
                        'ua850', 'ua700', 'ua500', 'ua200',
                        'ta850', 'ta700', 'ta500', 'ta200',
                        'va850', 'va700', 'va500', 'va200',
                        'hus850', 'hus700', 'hus500', 'hus200',
                        'hur850', 'hur700', 'hur500', 'hur200',
                        'zg500',
                        'ua_Atl_sect', 'va_Atl_sect', 'ta_Atl_sect', 'hus_Atl_sect',
                        'NO3', 'PO4', 'O2', 'Si',
                        'PO4_surf', 'O2_surf', 'Si_surf', 'NO3_surf',
                        'NO3_300m', 'PO4_300m', 'O2_300m', 'Si_300m',
                        'NO3_1000m', 'PO4_1000m', 'O2_1000m', 'Si_1000m',
                        'NO3_2500m', 'PO4_2500m', 'O2_2500m', 'Si_2500m',
                        'albvis', 'albnir', 'snow', 'gpp','gpptot', 'lai','LAI', 'fluxlat', 'fluxsens', 'pme']:
            project='ref_climatos'
        else:
            project='ref_ts'
    # -- dealing with a custom dictionary of obs (my_obs) 
    #if my_obs:
    #    for tmpproject in my_obs:
    #        for product in my_obs[tmpproject]:
    #            if variable in my_obs[tmpproject][product]:
    #               project = tmpproject 
    refs = {
        'ref_climatos' : {
            'CERES'  : [ 'rlut', 'rsut' , 'rlutcs', 'rsutcs', 'rlus', 'rsus' , 'rluscs', 'rsuscs', 'rlds', 'rsds', 'rsdscs','rldscs' ] ,
            'ERAINT' : [ 'tas', 'ta', 'psl', 'uas', 'vas' ,'hus','hur','huss', 'ua', 'va','wfo',
                         'ua850', 'ua700', 'ua500', 'ua200',
                         'ta850', 'ta700', 'ta500', 'ta200',
                         'va850', 'va700', 'va500', 'va200',
                         'hus850', 'hus700', 'hus500', 'hus200',
                         'hur850', 'hur700', 'hur500', 'hur200',
                         'zg500',
                         'ua_Atl_sect', 'va_Atl_sect', 'ta_Atl_sect', 'hus_Atl_sect',
                       ],
            'RSS'    : [ 'prw' ],
            'GPCP'   : ['pr'],
            'NSIDC'  : ['sic'],
            'WOA13-v2': ['thetao','so','to','tos','to200','to1000','to2000','so200','so1000','so2000'],
            'NODC-WOA09' : [ 'sos'],
            'WOA09': ['NO3', 'PO4', 'O2', 'Si',
                      'NO3_surf', 'PO4_surf', 'O2_surf', 'Si_surf',
                      'NO3_300m',  'PO4_300m', 'O2_300m', 'Si_300m',
                      'NO3_2500m', 'PO4_2500m', 'O2_2500m', 'Si_2500m',
                      'NO3_1000m', 'PO4_1000m', 'O2_1000m', 'Si_1000m',],
            'CNES-AVISO-L4': [ 'zos' ],
            'DeBoyerM' : ['mlotst','omlmax'],
            'CLARA-A1-1deg': ['alb'],
            'DASILVA': ['hurs'],
            'HOAPS3': ['hfls','hfss'],
            'LMDZ-OBS': ['tauu','tauv','pme','tauuo','tauvo'],
            'CERES-EBAF':['cltcalipso','clhcalipso','clmcalipso','cllcalipso'],
            'EnsembleGPP':['gpp','gpptot'],
            'GIMM3G':['lai','LAI'],
            'MODIS':['albnir','albvis','snow'],
            'EnsembleHcor':['fluxsens'],
            'EnsembleLEcor':['fluxlat'],
        },
        'ref_ts' : {
            'ERAInterim' : [ 'tas', 'psl' , 'uas' , 'vas', 'cldl', 'cldm', 'cldh' ], 
            'GPCP'   : [ 'pr'], 
            'CERES'  : [ 'rlut'  ,  'rsut'  ,      'rlutcs',   'rsutcs' ],
            'NCEP'   : [ 'huss' ],
            'MODIS-L3-C5' : ['clt'],
            'CLARA-A1-1deg': ['alb'],
            'NSIDC' : ['sic'],
        }
    }
    # -- Update the dictionary
    #refs.update(my_obs)
    if project in refs :
        for product in refs[project] :
            if variable in refs[project][product] :
               if project=='ref_climatos': return {'project':project,'product':product,'variable':variable, 'frequency':'annual_cycle'}
               if project=='ref_ts': return {'project':project,'product':product,'variable':variable, 'frequency':'monthly'}

