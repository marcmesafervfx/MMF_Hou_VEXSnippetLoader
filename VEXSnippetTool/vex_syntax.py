# VEX Keywords - Official list
VEX_KEYWORDS = [
    'break', 'const', 'continue', 'do', 'dict',
    'else', 'export', 'float', 'for', 'forpoints', 'foreach',
    'gather', 'if', 'illuminance', 'import', 'int',
    'matrix', 'matrix2', 'matrix3', 'return', 'string',
    'struct', 'vector', 'vector2', 'vector4',
    'void', 'while'
]

# VEX Functions - Complete list organized by categories
VEX_FUNCTIONS = [
    # Arrays
    'append', 'argsort', 'array', 'findlowerbound', 'findlowerboundsorted',
    'findsorted', 'insert', 'isvalidindex', 'len', 'pop', 'push',
    'removeindex', 'removevalue', 'reorder', 'resize', 'reverse', 'slice',
    'sort', 'upush',

    # Attributes and Intrinsics
    'addattrib', 'adddetailattrib', 'addpointattrib', 'addprimattrib',
    'addvertexattrib', 'addvisualizer', 'attrib', 'attribclass', 'attribdataid',
    'attribsize', 'attribtype', 'attribtypeinfo', 'curvearclen', 'detail',
    'detailattrib', 'detailattribsize', 'detailattribtype', 'detailattribtypeinfo',
    'detailintrinsic', 'findattribval', 'findattribvalcount', 'getattrib',
    'getattribute', 'hasattrib', 'hasdetailattrib', 'haspointattrib',
    'hasprimattrib', 'hasvertexattrib', 'idtopoint', 'idtoprim', 'nametopoint',
    'nametoprim', 'nuniqueval', 'point', 'pointattrib', 'pointattribsize',
    'pointattribtype', 'pointattribtypeinfo', 'pointlocaltransforms',
    'pointtransform', 'pointtransformrigid', 'pointtransforms',
    'pointtransformsrigid', 'prim', 'prim_attribute', 'primarclen', 'primattrib',
    'primattribsize', 'primattribtype', 'primattribtypeinfo', 'primduv',
    'priminteriorweights', 'primintrinsic', 'primuv', 'primuvconvert',
    'removedetailattrib', 'removepointattrib', 'removepointgroup',
    'removeprimattrib', 'removeprimgroup', 'removevertexattrib',
    'removevertexgroup', 'setattrib', 'setattribtypeinfo', 'setdetailattrib',
    'setdetailintrinsic', 'setpointattrib', 'setpointlocaltransforms',
    'setpointtransform', 'setpointtransforms', 'setprimattrib', 'setprimintrinsic',
    'setvertexattrib', 'uniqueval', 'uniquevals', 'uvsample', 'vertex',
    'vertexattrib', 'vertexattribsize', 'vertexattribtype', 'vertexattribtypeinfo',

    # BSDFs
    'albedo', 'ashikhmin', 'blinn', 'chiang', 'chiang_fur', 'cone', 'cvex_bsdf',
    'diffuse', 'eval_bsdf', 'getbounces', 'ggx', 'hair', 'henyeygreenstein',
    'isotropic', 'mask_bsdf', 'normal_bsdf', 'phong', 'phonglobe', 'sample_bsdf',
    'solid_angle', 'split_bsdf', 'sssapprox', 'specular',

    # CHOP
    'chadd', 'chattr', 'chattrnames', 'chend', 'chendf', 'chendt', 'chindex',
    'chinput', 'chinputlimits', 'chnames', 'chnumchan', 'chop', 'choplocal',
    'choplocalt', 'chopt', 'chrate', 'chreadbuf', 'chremove', 'chremoveattr',
    'chrename', 'chresizebuf', 'chsetattr', 'chsetlength', 'chsetrate',
    'chsetstart', 'chstart', 'chstartf', 'chstartt', 'chwritebuf', 'isframes',
    'issamples', 'isseconds', 'ninputs',

    # Channel Primitives
    'chprim_clear', 'chprim_destroykey', 'chprim_end', 'chprim_eval',
    'chprim_insertkey', 'chprim_keycount', 'chprim_keytimes', 'chprim_keyvalues',
    'chprim_length', 'chprim_setkeyaccel', 'chprim_setkeyslope',
    'chprim_setkeyvalue', 'chprim_start',

    # Color
    'blackbody', 'ctransform', 'luminance',

    # Conversion
    'atof', 'atoi', 'cracktransform', 'degrees', 'eulertoquaternion', 'hsvtorgb',
    'qconvert', 'quaterniontoeuler', 'radians', 'rgbtohsv', 'rgbtoxyz',
    'serialize', 'unserialize', 'xyztorgb',

    # Crowds
    'agentaddclip', 'agentchannelcount', 'agentchannelnames', 'agentchannelvalue',
    'agentchannelvalues', 'agentclipcatalog', 'agentclipchannel',
    'agentclipchannelnames', 'agentcliplayerblend', 'agentcliplength',
    'agentclipnames', 'agentclipsample', 'agentclipsamplelocal',
    'agentclipsamplerate', 'agentclipsampleworld', 'agentclipstarttime',
    'agentcliptimes', 'agentcliptransformgroups', 'agentclipweights',
    'agentcollisionlayer', 'agentcollisionlayers', 'agentcurrentlayer',
    'agentcurrentlayers', 'agentfindclip', 'agentfindlayer',
    'agentfindtransformgroup', 'agentlayerbindings', 'agentlayers',
    'agentlayershapes', 'agentlocaltransform', 'agentlocaltransforms',
    'agentmetadata', 'agentrestlocaltransform', 'agentrestworldtransform',
    'agentrigchildren', 'agentrigfind', 'agentrigfindchannel', 'agentrigparent',
    'agentsolvefbik', 'agenttransformcount', 'agenttransformgroupmember',
    'agenttransformgroupmemberchannel', 'agenttransformgroups',
    'agenttransformgroupweight', 'agenttransformnames', 'agenttransformtolocal',
    'agenttransformtoworld', 'agentworldtransform', 'agentworldtransforms',
    'setagentchannelvalue', 'setagentchannelvalues', 'setagentclipnames',
    'setagentclips', 'setagentcliptimes', 'setagentclipweights',
    'setagentcollisionlayer', 'setagentcollisionlayers', 'setagentcurrentlayer',
    'setagentcurrentlayers', 'setagentlocaltransform', 'setagentlocaltransforms',
    'setagentworldtransform', 'setagentworldtransforms',

    # Dict
    'json_dumps', 'json_loads', 'keys', 'typeid',

    # Displace
    'dimport',

    # File I/O
    'file_stat',

    # Filter
    'filter_remap',

    # Fuzzy Logic
    'fuzzify', 'fuzzy_and', 'fuzzy_defuzz_centroid', 'fuzzy_nand', 'fuzzy_nor',
    'fuzzy_not', 'fuzzy_nxor', 'fuzzy_or', 'fuzzy_xor',

    # Geometry
    'addpoint', 'addprim', 'addvertex', 'clip', 'geoself', 'geounwrap',
    'inedgegroup', 'intersect', 'intersect_all', 'minpos', 'nearpoint',
    'nearpoints', 'nedgesgroup', 'neighbour', 'neighbourcount', 'neighbours',
    'npoints', 'nprimitives', 'nvertices', 'nverticesgroup', 'pointprims',
    'pointvertex', 'pointvertices', 'polyneighbours', 'primfind', 'primpoint',
    'primpoints', 'primvertex', 'primvertexcount', 'primvertices', 'removeattrib',
    'removepoint', 'removeprim', 'removevertex', 'setedgegroup', 'setprimvertex',
    'setvertexpoint', 'uvintersect', 'vertexcurveparam', 'vertexindex',
    'vertexnext', 'vertexpoint', 'vertexprev', 'vertexprim', 'vertexprimindex',

    # Groups
    'expandedgegroup', 'expandpointgroup', 'expandprimgroup', 'expandvertexgroup',
    'inpointgroup', 'inprimgroup', 'invertexgroup', 'npointsgroup',
    'nprimitivesgroup', 'setpointgroup', 'setprimgroup', 'setvertexgroup',

    # Half-edges
    'hedge_dstpoint', 'hedge_dstvertex', 'hedge_equivcount', 'hedge_isequiv',
    'hedge_isprimary', 'hedge_isvalid', 'hedge_next', 'hedge_nextequiv',
    'hedge_postdstpoint', 'hedge_postdstvertex', 'hedge_presrcpoint',
    'hedge_presrcvertex', 'hedge_prev', 'hedge_prim', 'hedge_primary',
    'hedge_srcpoint', 'hedge_srcvertex', 'pointedge', 'pointhedge',
    'pointhedgenext', 'primhedge', 'vertexhedge',

    # Hex
    'hex_adjacent', 'hex_faceindex',

    # Image Processing
    'accessframe', 'alphaname', 'binput', 'bumpname', 'chname', 'cinput',
    'colorname', 'depthname', 'dsmpixel', 'finput', 'hasmetadata', 'hasplane',
    'iaspect', 'ichname', 'iend', 'iendtime', 'ihasplane', 'inumplanes',
    'iplaneindex', 'iplanename', 'iplanesize', 'irate', 'istart', 'istarttime',
    'ixres', 'iyres', 'lumname', 'maskname', 'metadata', 'ninput', 'normalname',
    'planeindex', 'planename', 'planesize', 'pointname', 'velocityname',

    # Interpolation
    'ckspline', 'clamp', 'cspline', 'efit', 'fit', 'fit01', 'fit10', 'fit11',
    'invlerp', 'lerp', 'lkspline', 'lspline', 'slerp', 'slerpv', 'smooth',

    # Light
    'ambient', 'atten', 'fastshadow', 'filtershadow',

    # Math
    'abs', 'acos', 'asin', 'atan', 'atan2', 'avg', 'cbrt', 'ceil',
    'combinelocaltransform', 'cos', 'cosh', 'cospi', 'cross', 'determinant',
    'diag', 'diagonalizesymmetric', 'distance_pointline', 'distance_pointray',
    'distance_pointsegment', 'dot', 'Du', 'Dv', 'Dw', 'eigenvalues', 'erf',
    'erf_inv', 'erfc', 'exp', 'extractlocaltransform', 'floor', 'frac', 'ident',
    'invert', 'isfinite', 'isinf', 'isnan', 'kspline', 'length', 'length2',
    'log', 'log10', 'makebasis', 'max', 'min', 'norm_1', 'norm_fro', 'norm_inf',
    'norm_max', 'norm_spectral', 'normalize', 'outerproduct', 'pinvert',
    'planesphereintersect', 'pow', 'predicate_incircle', 'predicate_insphere',
    'predicate_orient2d', 'predicate_orient3d', 'premul', 'product', 'ptlined',
    'qdistance', 'qinvert', 'qmultiply', 'qrotate', 'quaternion',
    'resample_linear', 'rint', 'shl', 'shr', 'shrz', 'sign', 'sin', 'sinh',
    'sinpi', 'slideframe', 'solvecubic', 'solvepoly', 'solvequadratic',
    'solvetriangleSSS', 'spline', 'spline_cdf', 'sqrt', 'sum', 'svddecomp',
    'tan', 'tanh', 'tanpi', 'tr', 'transpose', 'trunc',

    # Measure
    'distance', 'distance2', 'getbbox', 'getbbox_center', 'getbbox_max',
    'getbbox_min', 'getbbox_size', 'getbounds', 'getpointbbox',
    'getpointbbox_center', 'getpointbbox_max', 'getpointbbox_min',
    'getpointbbox_size', 'planepointdistance', 'relbbox', 'relpointbbox',
    'surfacedist', 'uvdist', 'windingnumber', 'windingnumber2d', 'xyzdist',

    # Metaball
    'metaimport', 'metamarch', 'metanext', 'metastart', 'metaweight',

    # Nodes
    'addvariablename', 'ch', 'ch2', 'ch3', 'ch4', 'chdict', 'chexpr', 'chexprf',
    'chexprt', 'chf', 'chi', 'chid', 'chp', 'chramp', 'chrampderiv', 'chs',
    'chsop', 'chsraw', 'chu', 'chv', 'cregioncapturetransform',
    'cregiondeformtransform', 'cregionoverridetransform', 'isconnected',
    'opfullpath', 'opid', 'opparentbonetransform', 'opparenttransform',
    'opparmtransform', 'oppreconstrainttransform', 'oppreparmtransform',
    'opprerawparmtransform', 'oppretransform', 'oprawparmtransform', 'optransform',

    # Noise and Randomness
    'anoise', 'curlgxnoise', 'curlgxnoise2d', 'curlnoise', 'curlnoise2d',
    'curlxnoise', 'curlxnoise2d', 'cwnoise', 'flownoise', 'flowpnoise',
    'gxnoise', 'gxnoised', 'hscript_noise', 'hscript_rand', 'hscript_snoise',
    'hscript_sturb', 'hscript_turb', 'mwnoise', 'mx_cellnoise', 'mx_perlin',
    'mx_voronoi', 'mx_worley', 'noise', 'noised', 'nrandom', 'onoise', 'pnoise',
    'pxnoised', 'rand', 'random', 'random_brj', 'random_fhash', 'random_ihash',
    'random_poisson', 'random_shash', 'random_sobol', 'snoise', 'vnoise',
    'wnoise', 'xnoise', 'xnoised',

    # Normals
    'computenormal', 'prim_normal',

    # Open Color IO
    'ocio_activedisplays', 'ocio_activeviews', 'ocio_import',
    'ocio_parsecolorspace', 'ocio_roles', 'ocio_spaces', 'ocio_transform',
    'ocio_transformview',

    # Particles
    'filamentsample',

    # Point Clouds and 3D Images
    'mattrib', 'mdensity', 'mspace', 'pcclose', 'pccone', 'pccone_radius',
    'pcconvex', 'pcexport', 'pcfarthest', 'pcfilter', 'pcfind', 'pcfind_radius',
    'pcgenerate', 'pcimport', 'pcimportbyidx3', 'pcimportbyidx4',
    'pcimportbyidxf', 'pcimportbyidxi', 'pcimportbyidxp', 'pcimportbyidxs',
    'pcimportbyidxv', 'pciterate', 'pcline', 'pcline_radius', 'pcnumfound',
    'pcopen', 'pcopenlod', 'pcsampleleaf', 'pcsegment', 'pcsegment_radius',
    'pcsize', 'pcunshaded', 'pcwrite', 'pgfind', 'photonmap', 'texture3d',
    'texture3dBox',

    # Sampling
    'create_cdf', 'create_pdf', 'limit_sample_space', 'newsampler', 'nextsample',
    'sample_cauchy', 'sample_cdf', 'sample_circle_arc',
    'sample_circle_edge_uniform', 'sample_circle_ring_uniform',
    'sample_circle_slice', 'sample_circle_uniform', 'sample_direction_cone',
    'sample_direction_uniform', 'sample_discrete', 'sample_exponential',
    'sample_geometry', 'sample_hemisphere', 'sample_hypersphere_cone',
    'sample_hypersphere_uniform', 'sample_light', 'sample_lognormal',
    'sample_lognormal_by_median', 'sample_normal', 'sample_orientation_cone',
    'sample_orientation_uniform', 'sample_photon', 'sample_sphere_cone',
    'sample_sphere_shell_uniform', 'sample_sphere_uniform', 'sampledisk',
    'variance',

    # Sensor Input
    'sensor_panorama_create', 'sensor_panorama_getcolor',
    'sensor_panorama_getcone', 'sensor_panorama_getdepth', 'sensor_save',

    # Shading and Rendering
    'area', 'blinnBRDF', 'bouncelabel', 'bouncemask', 'diffuseBRDF', 'filterstep',
    'fresnel', 'frontface', 'gather', 'getblurP', 'getcomponents', 'getderiv',
    'getfogname', 'getglobalraylevel', 'getgroupid', 'getlight', 'getlightid',
    'getlightname', 'getlights', 'getlightscope', 'getlocalcurvature',
    'getmaterial', 'getmaterialid', 'getobjectid', 'getobjectname',
    'getphotonlight', 'getprimid', 'getptextureid', 'getraylevel', 'getrayweight',
    'getsamplestore', 'getscope', 'getsmoothP', 'getuvtangents', 'gradient',
    'haslight', 'illuminance', 'integratehoseksky', 'interpolate',
    'intersect_lights', 'irradiance', 'isfogray', 'islpeactive', 'israytracing',
    'isshadingRHS', 'isshadowray', 'isuvrendering', 'lightbounces', 'lightid',
    'lightstate', 'limport', 'matchvex_blinn', 'matchvex_specular',
    'nbouncetypes', 'objectstate', 'occlusion', 'pathtrace', 'phongBRDF',
    'rayhittest', 'rayimport', 'reflect', 'reflectlight', 'refract',
    'refractlight', 'renderstate', 'resolvemissedray', 'scatter',
    'setcurrentlight', 'setsamplestore', 'shadow', 'shadow_light', 'shimport',
    'simport', 'specularBRDF', 'storelightexport', 'switch', 'trace',
    'translucent', 'uvunwrap', 'wireblinn', 'wirediffuse', 'writepixel',

    # Strings
    'abspath', 'chr', 'concat', 'decode', 'decodeattrib', 'decodeparm',
    'decodeutf8', 'encode', 'encodeattrib', 'encodeparm', 'encodeutf8',
    'endswith', 'find', 'isalpha', 'isdigit', 'itoa', 'join', 'lstrip',
    'makevalidvarname', 'match', 'opdigits', 'ord', 'pluralize', 're_find',
    're_findall', 're_match', 're_replace', 're_split', 'relativepath',
    'relpath', 'replace', 'replace_match', 'rstrip', 'split', 'splitpath',
    'sprintf', 'startswith', 'strip', 'strlen', 'titlecase', 'tolower', 'toupper',

    # Subdivision Surfaces
    'osd_facecount', 'osd_firstpatch', 'osd_limitsurface',
    'osd_limitsurfacevertex', 'osd_lookupface', 'osd_lookuppatch',
    'osd_patchcount', 'osd_patches',

    # Tetrahedrons
    'tet_adjacent', 'tet_faceindex',

    # Texturing
    'colormap', 'depthmap', 'environment', 'expand_udim', 'has_udim',
    'importance_remap', 'ocean_sample', 'ptexture', 'rawcolormap', 'shadowmap',
    'teximport', 'texprintf', 'texture',

    # Transforms and Space
    'dihedral', 'fromNDC', 'getpackedtransform', 'getspace', 'instance', 'lookat',
    'maketransform', 'ndcdepth', 'ntransform', 'orthographic', 'ow_nspace',
    'ow_space', 'ow_vspace', 'packedtransform', 'perspective', 'polardecomp',
    'prerotate', 'prescale', 'pretranslate', 'ptransform', 'rotate', 'rotate_x_to',
    'scale', 'setpackedtransform', 'smoothrotation', 'solveconstraint',
    'solvecurve', 'solvefbik', 'solveik', 'solvephysfbik', 'toNDC', 'translate',
    'tw_nspace', 'tw_space', 'tw_vspace', 'vtransform', 'wo_nspace', 'wo_space',
    'wo_vspace', 'wt_nspace', 'wt_space', 'wt_vspace',

    # USD
    'usd_addattrib', 'usd_addcollectionexclude', 'usd_addcollectioninclude',
    'usd_addinversetotransformorder', 'usd_addorient', 'usd_addprim',
    'usd_addprimvar', 'usd_addrelationshiptarget', 'usd_addrotate',
    'usd_addscale', 'usd_addschemaattrib', 'usd_addtotransformorder',
    'usd_addtransform', 'usd_addtranslate', 'usd_applyapi', 'usd_attrib',
    'usd_attribelement', 'usd_attriblen', 'usd_attribnames', 'usd_attribsize',
    'usd_attribtimesamples', 'usd_attribtypename', 'usd_blockattrib',
    'usd_blockprimvar', 'usd_blockprimvarindices', 'usd_blockrelationship',
    'usd_boundmaterialpath', 'usd_childnames', 'usd_clearmetadata',
    'usd_cleartransformorder', 'usd_collectioncomputedpaths',
    'usd_collectioncontains', 'usd_collectionexcludes',
    'usd_collectionexpansionrule', 'usd_collectionincludes', 'usd_drawmode',
    'usd_findtransformname', 'usd_flattenediprimvar',
    'usd_flattenediprimvarelement', 'usd_flattenedprimvar',
    'usd_flattenedprimvarelement', 'usd_getbbox', 'usd_getbbox_center',
    'usd_getbbox_max', 'usd_getbbox_min', 'usd_getbbox_size', 'usd_getbounds',
    'usd_getpointinstancebounds', 'usd_hasapi', 'usd_haspayload',
    'usd_iprimvar', 'usd_iprimvarelement', 'usd_iprimvarelementsize',
    'usd_iprimvarindices', 'usd_iprimvarinterpolation', 'usd_iprimvarlen',
    'usd_iprimvarnames', 'usd_iprimvarsize', 'usd_iprimvartimesamples',
    'usd_iprimvartypename', 'usd_isabstract', 'usd_isactive', 'usd_isarray',
    'usd_isarrayiprimvar', 'usd_isarraymetadata', 'usd_isarrayprimvar',
    'usd_isattrib', 'usd_iscollection', 'usd_iscollectionpath',
    'usd_isindexediprimvar', 'usd_isindexedprimvar', 'usd_isinstance',
    'usd_isiprimvar', 'usd_iskind', 'usd_ismetadata', 'usd_ismodel',
    'usd_isprim', 'usd_isprimvar', 'usd_isrelationship', 'usd_isstage',
    'usd_istransformreset', 'usd_istype', 'usd_isvisible', 'usd_kind',
    'usd_localtransform', 'usd_makeattribpath', 'usd_makecollectionpath',
    'usd_makepropertypath', 'usd_makerelationshippath', 'usd_makevalidprimname',
    'usd_makevalidprimpath', 'usd_metadata', 'usd_metadataelement',
    'usd_metadatalen', 'usd_metadatanames', 'usd_name', 'usd_parentpath',
    'usd_pointinstance_getbbox', 'usd_pointinstance_getbbox_center',
    'usd_pointinstance_getbbox_max', 'usd_pointinstance_getbbox_min',
    'usd_pointinstance_getbbox_size', 'usd_pointinstance_relbbox',
    'usd_pointinstancetransform', 'usd_primvar', 'usd_primvarattribname',
    'usd_primvarelement', 'usd_primvarelementsize', 'usd_primvarindices',
    'usd_primvarinterpolation', 'usd_primvarlen', 'usd_primvarnames',
    'usd_primvarsize', 'usd_primvartimesamples', 'usd_primvartypename',
    'usd_purpose', 'usd_relationshipforwardedtargets', 'usd_relationshipnames',
    'usd_relationshiptargets', 'usd_relbbox', 'usd_removerelationshiptarget',
    'usd_setactive', 'usd_setattrib', 'usd_setattribelement',
    'usd_setcollectionexcludes', 'usd_setcollectionexpansionrule',
    'usd_setcollectionincludes', 'usd_setdrawmode', 'usd_setkind',
    'usd_setmetadata', 'usd_setmetadataelement', 'usd_setprimvar',
    'usd_setprimvarelement', 'usd_setprimvarelementsize',
    'usd_setprimvarindices', 'usd_setprimvarinterpolation', 'usd_setpurpose',
    'usd_setrelationshiptargets', 'usd_settransformorder',
    'usd_settransformreset', 'usd_setvariantselection', 'usd_setvisibility',
    'usd_setvisible', 'usd_specifier', 'usd_transformname',
    'usd_transformorder', 'usd_transformsuffix', 'usd_transformtype',
    'usd_typename', 'usd_uniquetransformname', 'usd_variants',
    'usd_variantselection', 'usd_variantsets', 'usd_worldtransform',

    # Utility
    'assert_enabled', 'assign', 'error', 'forpoints', 'getcomp', 'isbound',
    'isvarying', 'opend', 'opstart', 'pack_inttosafefloat', 'print_once',
    'printf', 'ramp_lookup', 'ramp_pack', 'ramp_unpack', 'select', 'set',
    'setcomp', 'sleep', 'swizzle', 'unpack_intfromsafefloat', 'warning',

    # Volume
    'volume', 'volumecubicsample', 'volumecubicsamplev', 'volumegradient',
    'volumeindex', 'volumeindexactive', 'volumeindexi', 'volumeindexorigin',
    'volumeindexp', 'volumeindextopos', 'volumeindexu', 'volumeindexv',
    'volumepostoindex', 'volumeres', 'volumesample', 'volumesamplei',
    'volumesamplep', 'volumesampleu', 'volumesamplev', 'volumesmoothsample',
    'volumesmoothsamplev', 'volumetypeid', 'volumevoxeldiameter',

    # Weight Array
    'weightarrayblend', 'weightarrayfromname', 'weightarraynormalize',
    'weightarraythreshold'
]
